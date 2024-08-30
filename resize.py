import os
from PIL import Image # 画像処理ライブラリPillow

def resize_image(image, max_width, max_height):
	width_ratio = max_width / image.width
	height_ratio = max_height / image.height
	resize_ratio = min(width_ratio, height_ratio)
	new_width = int(image.width * resize_ratio)
	new_height = int(image.height * resize_ratio)
	return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

def resize_images_in_folder(folder_path, max_width=550, max_height=760):# 目標の画像サイズ設定
	for root, _, files in os.walk(folder_path):#再起検索せずにフォルダ内のファイルを掘るwalk関数
		for filename in files:
			if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
				image_path = os.path.join(root, filename)
				try:
					with Image.open(image_path) as img:
						resized_img = resize_image(img, max_width, max_height)
						resized_img.save(image_path)
						print(f'Resized and saved: {filename} in {root}')
				except Exception as e:
					print(f"Failed to process {filename} in {root}: {e}")

folder_path = '/foldername/test/'  # ここに対象フォルダの絶対パスを指定してください
resize_images_in_folder(folder_path)
