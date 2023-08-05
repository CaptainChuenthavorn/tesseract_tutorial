num_images = 100
image_prefix = "tesstrain/data/Prompt-ground-truth/tha_"
gt_prefix = "tesstrain/data/Prompt-ground-truth/tha_"

# Generate the list of lines for the list.train file
lines = [f"{image_prefix}{i}.tif {gt_prefix}{i}.gt.txt" for i in range(num_images)]

# Join the lines with newline characters to create the complete text
list_train_text = "\n".join(lines)

# Write the text to the list.train file
with open("listtrain.txt", "w", encoding="utf-8") as file:
    file.write(list_train_text)
