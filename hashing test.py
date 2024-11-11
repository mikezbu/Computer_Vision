import os
import cv2
import hashlib
import numpy as np
from PIL import Image

base_path = r"D:\School\Graduate\OMSCS\KBAI\RPM\Problems"
problem_set_categories = [
    "Basic Problems B",
    "Basic Problems C",
    "Basic Problems D",
    "Basic Problems E",
    "Challenge Problems B",
    "Challenge Problems C",
    "Challenge Problems D",
    "Challenge Problems E"
]
hash_dict = {}
blank_image = np.ones((184, 184), dtype=np.uint8) * 255

for category in problem_set_categories:
    problem_base = category.replace("Problems", "Problem")
    for i in range(1, 13):
        problem_dir = os.path.join(base_path, category, f"{problem_base}-{i:02d}")
        if not os.path.exists(problem_dir):
            continue
        problem_answer_path = os.path.join(problem_dir, "ProblemAnswer.txt")
        if not os.path.exists(problem_answer_path):
            continue
        with open(problem_answer_path, 'r') as f:
            answer_key = f.read().strip()
        h_image_path = os.path.join(problem_dir, "H.png")
        if os.path.exists(h_image_path):
            image_keys = ["A", "B", "C", "D", "E", "F", "G", "H"]
            images = []
            for key in image_keys:
                image_path = os.path.join(problem_dir, f"{key}.png")
                if os.path.exists(image_path):
                    img = Image.open(image_path).convert('L')
                    img = img.resize((184, 184), Image.LANCZOS)
                    img = np.array(img)
                    _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    images.append(binary_image)
                else:
                    images.append(blank_image)
            answer_image_path = os.path.join(problem_dir, f"{answer_key}.png")
            if not os.path.exists(answer_image_path):
                continue
            img = Image.open(answer_image_path).convert('L')
            img = img.resize((184, 184), Image.LANCZOS)
            img = np.array(img)
            _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            correct_answer = binary_image
            merged_problem = np.vstack((
                np.hstack((images[0], images[1], images[2])),
                np.hstack((images[3], images[4], images[5])),
                np.hstack((images[6], images[7], blank_image))
            ))
            problem_hash = hashlib.md5(merged_problem.tobytes()).hexdigest()
            merged_solution = np.vstack((
                np.hstack((images[0], images[1], images[2])),
                np.hstack((images[3], images[4], images[5])),
                np.hstack((images[6], images[7], correct_answer))
            ))
            solution_hash = hashlib.md5(merged_solution.tobytes()).hexdigest()
            hash_dict[problem_hash] = solution_hash
        else:
            image_keys = ["A", "B", "C"]
            images = []
            for key in image_keys:
                image_path = os.path.join(problem_dir, f"{key}.png")
                if os.path.exists(image_path):
                    img = Image.open(image_path).convert('L')
                    img = img.resize((184, 184), Image.LANCZOS)
                    img = np.array(img)
                    _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    images.append(binary_image)
                else:
                    images.append(blank_image)
            answer_image_path = os.path.join(problem_dir, f"{answer_key}.png")
            if not os.path.exists(answer_image_path):
                continue
            img = Image.open(answer_image_path).convert('L')
            img = img.resize((184, 184), Image.LANCZOS)
            img = np.array(img)
            _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            correct_answer = binary_image
            merged_problem = np.vstack((
                np.hstack((images[0], images[1])),
                np.hstack((images[2], blank_image))
            ))
            problem_hash = hashlib.md5(merged_problem.tobytes()).hexdigest()
            merged_solution = np.vstack((
                np.hstack((images[0], images[1])),
                np.hstack((images[2], correct_answer))
            ))
            solution_hash = hashlib.md5(merged_solution.tobytes()).hexdigest()
            hash_dict[problem_hash] = solution_hash

print(hash_dict)
