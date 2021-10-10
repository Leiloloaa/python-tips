import os
root, dirs, files = next(os.walk("tips_3/"))
idx = 0
for item in files:
    old_file_path = os.path.join(root, item)
    new_file_path = os.path.join(root, f"py_{idx}.jpg")
    os.rename(old_file_path, new_file_path)
    idx = idx + 1
