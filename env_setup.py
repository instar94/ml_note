import builtins
import platform
import subprocess

# ── 환경 감지 ─────────────────────────────────────────────────────────────────


def _detect_env():
    try:
        import google.colab  # noqa: F401

        return "colab"
    except ImportError:
        pass
    if platform.system() == "Windows":
        return "windows"
    return "other"


ENV = _detect_env()

# ── 한글 폰트 설정 ────────────────────────────────────────────────────────────


def _setup_font():
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    if ENV == "colab":
        subprocess.run(
            ["apt-get", "install", "-y", "fonts-nanum"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        import matplotlib.font_manager as fm

        fm._load_fontmanager(try_read_cache=False)
        plt.rcParams["font.family"] = "NanumGothic"
    elif ENV == "windows":
        plt.rcParams["font.family"] = "Malgun Gothic"

    mpl.rcParams["axes.unicode_minus"] = False


_setup_font()

# ── 헬퍼 함수 ─────────────────────────────────────────────────────────────────


def _upload_csv():
    """Colab: 파일 업로드 다이얼로그 → dict[filename: str] = pd.DataFrame"""
    import pandas as pd
    from google.colab import files

    uploaded = files.upload()
    return {
        name: pd.read_csv(__import__("io").BytesIO(data))
        for name, data in uploaded.items()
    }


def _download_kaggle(competition: str, path: str = "./data"):
    """Windows: kaggle CLI로 competition 데이터 다운로드 후 압축 해제"""
    import os
    import zipfile

    os.makedirs(path, exist_ok=True)
    subprocess.run(
        ["kaggle", "competitions", "download", "-c", competition, "-p", path],
        check=True,
    )
    for fname in os.listdir(path):
        if fname.endswith(".zip"):
            zip_path = os.path.join(path, fname)
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(path)
            os.remove(zip_path)
    print(f"[download_kaggle] '{competition}' 데이터 → {path}")


def _git_push(msg: str):
    """Colab 전용: GITHUB_TOKEN 시크릿으로 git add/commit/push"""
    import re

    from google.colab import userdata

    token = userdata.get("GITHUB_TOKEN")

    remote_url = subprocess.check_output(
        ["git", "remote", "get-url", "origin"], text=True
    ).strip()

    # https://github.com/... → https://<token>@github.com/...
    auth_url = re.sub(r"https://", f"https://{token}@", remote_url)
    subprocess.run(["git", "remote", "set-url", "origin", auth_url], check=True)

    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push"], check=True)

    # 토큰 제거 후 원래 URL 복원
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)
    print(f"[git_push] '{msg}' 푸시 완료")


# ── builtins 등록 ─────────────────────────────────────────────────────────────

if ENV == "colab":
    builtins.upload_csv = _upload_csv
    builtins.git_push = _git_push
elif ENV == "windows":
    builtins.download_kaggle = _download_kaggle

print(f"[env_setup] 환경: {ENV} | 한글 폰트 설정 완료")
