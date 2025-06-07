import subprocess
import sys
import platform
import torch

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def install_torch():
    torch_version = "2.6.0"
    torchvision = "torchvision"
    torchaudio = "torchaudio"

    try:
        if not torch.cuda.is_available():
            print("?? No CUDA-capable GPU detected. Installing CPU-only torch...")
            run(f"pip install torch=={torch_version}")
            return
    except:
        print("??? PyTorch not installed yet, cannot auto-detect CUDA. Trying NVIDIA tools...")

    # Fallback detection using nvidia-smi (works before torch is installed)
    try:
        output = subprocess.check_output("nvidia-smi", shell=True).decode()
        if "CUDA Version: 12" in output:
            index_url = "https://download.pytorch.org/whl/cu121"
        elif "CUDA Version: 11" in output:
            index_url = "https://download.pytorch.org/whl/cu118"
        else:
            print("?? Unknown or unsupported CUDA version, defaulting to cu118.")
            index_url = "https://download.pytorch.org/whl/cu118"
    except:
        print("? Unable to detect CUDA version with nvidia-smi. Falling back to CPU install.")
        run(f"pip install torch=={torch_version}")
        return

    # Install with selected CUDA
    print(f"? Installing torch {torch_version} with index {index_url}")
    run(f"pip install torch=={torch_version} {torchvision} {torchaudio} --index-url {index_url}")

if __name__ == "__main__":
    pip install -r requirements.txt
    install_torch()
