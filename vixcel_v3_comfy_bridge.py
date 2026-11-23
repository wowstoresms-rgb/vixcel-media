#!/usr/bin/env python3
"""
VIXCEL MEDIA V3 — Local & Google Colab Open-Source AI Bridge
Supports: ComfyUI, PaddleOCR, Docling, Real-ESRGAN, MuseTalk, LivePortraitKJ, UVR
Optimized for Windows 11 (8GB RAM / Intel Iris Xe CPU mode) & Free Google Colab T4 GPU.
"""
import os, sys, json, subprocess

MODULES = {
    "comfyui": {"repo": "https://github.com/Comfy-Org/ComfyUI.git", "dir": "ComfyUI", "vram": "4GB+ (or --cpu)"},
    "vhs": {"repo": "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git", "dir": "ComfyUI/custom_nodes/ComfyUI-VideoHelperSuite"},
    "liveportrait": {"repo": "https://github.com/kijai/ComfyUI-LivePortraitKJ.git", "dir": "ComfyUI/custom_nodes/ComfyUI-LivePortraitKJ"},
    "musetalk": {"repo": "https://github.com/TMElyralab/MuseTalk.git", "dir": "MuseTalk"},
    "realesrgan": {"repo": "https://github.com/xinntao/Real-ESRGAN.git", "dir": "Real-ESRGAN"},
    "paddleocr": {"pip": "paddlepaddle paddleocr"},
    "docling": {"pip": "docling"},
    "uvr": {"pip": "audio-separator[cpu]"}
}

def lazy_install(module_key):
    if module_key not in MODULES:
        print(f"Unknown module: {module_key}")
        return
    info = MODULES[module_key]
    print(f"[VIXCEL V3] Lazy installing {module_key}...")
    if "repo" in info and not os.path.exists(info["dir"]):
        subprocess.run(["git", "clone", "--depth", "1", info["repo"], info["dir"]], check=False)
    if "pip" in info:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q"] + info["pip"].split(), check=False)
    print(f"[VIXCEL V3] {module_key} ready.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        lazy_install(sys.argv[1])
    else:
        print("VIXCEL V3 Bridge Ready. Usage: python vixcel_v3_comfy_bridge.py <module_name>")
