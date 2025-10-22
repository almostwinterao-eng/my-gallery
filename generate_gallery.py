import os

# 支持的图片格式
img_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

# 获取当前目录所有图片
images = [f for f in os.listdir('.') if f.lower().endswith(img_extensions)]
images.sort()

# ---------- 生成首页 index.html ----------
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Image Gallery</title>
<style>
body {
    background: #111;
    color: #fff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
    gap: 20px;
}
img {
    width: 250px;
    height: 250px;
    object-fit: cover;
    border-radius: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
}
img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(255,255,255,0.4);
}
</style>
</head>
<body>
<h1>My Image Gallery</h1>
"""

for img in images:
    name = os.path.splitext(img)[0]
    index_html += f'<a href="{name}.html"><img src="{img}" alt="{name}"></a>\n'

index_html += """
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"✅ 已生成首页 index.html，包含 {len(images)} 张图片。")

# ---------- 生成每张图片独立页面 ----------
for img in images:
    name = os.path.splitext(img)[0]
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{
    background: #111;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}
img {{
    max-width: 90%;
    max-height: 90%;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(255,255,255,0.3);
}}
a {{
    position: fixed;
    top: 20px;
    left: 20px;
    color: #fff;
    text-decoration: none;
    font-size: 18px;
    background: rgba(0,0,0,0.5);
    padding: 5px 10px;
    border-radius: 5px;
}}
a:hover {{
    background: rgba(0,0,0,0.8);
}}
</style>
</head>
<body>
<a href="index.html">← Back</a>
<img src="{img}" alt="{name}">
</body>
</html>
"""
    with open(f"{name}.html", "w", encoding="utf-8") as f:
        f.write(page_html)

print(f"✅ 已生成 {len(images)} 张独立图片页面。")
