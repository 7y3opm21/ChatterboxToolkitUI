import subprocess
import sys
import os

TORCH_VERSION = "2.6.0"
TORCH_INDEX_URL = "https://download.pytorch.org/whl/cu118"

def run(cmd):
    print(f"\n {cmd}\n{'-'*60}")
    subprocess.run(cmd, shell=True, check=True)

def install_requirements():
    if not os.path.exists("requirements.txt"):
        print("requirements.txt not found.")
        sys.exit(1)

    print("Installing project requirements (including torch)...")
    run("pip install -r requirements.txt --verbose")

def uninstall_existing_torch():
    print("Uninstalling any existing torch/vision/audio versions...")
    run("pip uninstall -y torch torchvision torchaudio")

def install_torch_cuda():
    print("Installing torch==2.6.0 with CUDA 11.8 (cu118)...")
    run(f"pip install torch=={TORCH_VERSION} torchvision torchaudio --index-url {TORCH_INDEX_URL} --verbose")

if __name__ == "__main__":
    install_requirements()
    uninstall_existing_torch()
    install_torch_cuda()
    print("\n Setup complete.")
