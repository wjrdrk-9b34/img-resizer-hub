#!/usr/bin/env python3
"""Batch resize gambar (butuh Pillow)."""
from PIL import Image
import sys, os
w = int(sys.argv[2]) if len(sys.argv) > 2 else 1280
folder = sys.argv[1] if len(sys.argv) > 1 else "."
for f in os.listdir(folder):
      if not f.lower().endswith((".jpg",".jpeg",".png")): continue
            p = os.path.join(folder, f); im = Image.open(p)
    r = w / im.width
    im = im.resize((w, int(im.height * r)))
    im.save(os.path.join(folder, "rs_" + f))
    print("resized:", f)
