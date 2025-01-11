import cv2
def add_text_with_background(image, text, position, font, font_scale, font_thickness, text_color, bg_color, opacity, padding=10):
    overlay = image.copy()
    text_size, baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_width, text_height = text_size
    rect_x1 = position[0] - padding
    rect_y1 = position[1] - text_height - padding
    rect_x2 = position[0] + text_width + padding
    rect_y2 = position[1] + baseline + padding
    cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), bg_color, -1)
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)
    cv2.putText(image, text, position, font, font_scale, text_color, font_thickness)
def draw_rectangle(image, top_left, bottom_right, color, thickness):
    cv2.rectangle(image, top_left, bottom_right, color, thickness)
image = cv2.imread('assignment-001-given.jpg')
text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 5
text_color = (0, 255, 0)
bg_color = (0, 0, 0)
opacity = 0.5
padding = 120
img_height, img_width, _ = image.shape
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_width, text_height = text_size
text_x = img_width - text_width - padding
text_y = text_height + padding
add_text_with_background(image, text, (text_x, text_y), font, font_scale, font_thickness, text_color, bg_color, opacity)
draw_rectangle(image, (200, 200), (950, 950), (0, 255, 0), 10)
cv2.imshow('Image Assignment', image)
cv2.waitKey(0)
cv2.imwrite('assignment-001-result.jpg', image)
cv2.destroyAllWindows()