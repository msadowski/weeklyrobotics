#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import yaml
import glob
import os

filename = "img_4"

issue_yaml = ""
list_of_files = glob.glob('../../_posts/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print latest_file
with open(latest_file) as infile:
    copy = False
    for line in infile:
        if line.strip() == "---" and not copy:
            copy = True
            continue
        elif line.strip() == "---":
            copy = False
            continue
        elif copy:
            issue_yaml += line

try:
    parsed_issue_yaml = yaml.load(issue_yaml)
except yaml.YAMLError as exc:
    print(exc)
    exit()

if parsed_issue_yaml["idx"]:
    title = parsed_issue_yaml["title"] +" #" + str(parsed_issue_yaml["idx"])
else:
    # title = parsed_issue_yaml["title"]
    print "ISSUES WITHOUT IDX ARE NOT SUPPORTED YET"

#setting varibles
idx = parsed_issue_yaml["idx"]
imgFile = "img/"+filename+".jpg"
yamlFile = "img/"+filename+".yaml"
output = "../../img/headers/" + str(idx) + ".jpg"
text = "Weekly Robotics #" + str(idx)
textColor = 'white'
shadowColor = 'black'
outlineAmount = 3
imgFraction = 0.8

#open yaml file
with open(yamlFile, 'r') as stream:
    try:
        parsedYaml = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

#open image
img = Image.open(imgFile)
draw = ImageDraw.Draw(img)

fontSize = 1
font = ImageFont.truetype("Roboto-Regular.ttf", fontSize)
while font.getsize(text)[0] < imgFraction*img.size[0]:
    fontSize += 1
    font = ImageFont.truetype("Roboto-Regular.ttf", fontSize)

fontSize -= 1

txtWidth, txtHeight = draw.textsize(text, font=font)

#get the size of the image
imgWidth,imgHeight = img.size

#get location to place text
x = (imgWidth - txtWidth)/2
y = (imgHeight - txtHeight)/2

#create outline text
for adj in range(outlineAmount):
    #move right
    draw.text((x-adj, y), text, font=font, fill=shadowColor)
    #move left
    draw.text((x+adj, y), text, font=font, fill=shadowColor)
    #move up
    draw.text((x, y+adj), text, font=font, fill=shadowColor)
    #move down
    draw.text((x, y-adj), text, font=font, fill=shadowColor)
    #diagnal left up
    draw.text((x-adj, y+adj), text, font=font, fill=shadowColor)
    #diagnal right up
    draw.text((x+adj, y+adj), text, font=font, fill=shadowColor)
    #diagnal left down
    draw.text((x-adj, y-adj), text, font=font, fill=shadowColor)
    #diagnal right down
    draw.text((x+adj, y-adj), text, font=font, fill=shadowColor)

#create normal text on image
draw.text((x,y), text, font=font, fill=textColor)

# yaml draw
font = ImageFont.truetype("Roboto-Regular.ttf", 14)
creditText = "Credit: " + parsedYaml['copyright']
txtWidth, txtHeight = draw.textsize(creditText, font=font)
x = imgWidth - txtWidth - 5
y = imgHeight - txtHeight - 20
for adj in range(outlineAmount):
    #move right
    draw.text((x-adj, y), creditText, font=font, fill=shadowColor)
    #move left
    draw.text((x+adj, y), creditText, font=font, fill=shadowColor)
    #move up
    draw.text((x, y+adj), creditText, font=font, fill=shadowColor)
    #move down
    draw.text((x, y-adj), creditText, font=font, fill=shadowColor)
    #diagnal left up
    draw.text((x-adj, y+adj), creditText, font=font, fill=shadowColor)
    #diagnal right up
    draw.text((x+adj, y+adj), creditText, font=font, fill=shadowColor)
    #diagnal left down
    draw.text((x-adj, y-adj), creditText, font=font, fill=shadowColor)
    #diagnal right down
    draw.text((x+adj, y-adj), creditText, font=font, fill=shadowColor)
# draw.rectangle(((x-3, y-3), (imgWidth, imgHeight)), fill="black")
draw.text((x,y), creditText, font=font, fill=textColor)

font = ImageFont.truetype("Roboto-Regular.ttf", 10)
linkText = parsedYaml['link']
txtWidth, txtHeight = draw.textsize(linkText, font=font)
x = imgWidth - txtWidth - 5
y = imgHeight - txtHeight - 5
for adj in range(outlineAmount):
    #move right
    draw.text((x-adj, y), linkText, font=font, fill=shadowColor)
    #move left
    draw.text((x+adj, y), linkText, font=font, fill=shadowColor)
    #move up
    draw.text((x, y+adj), linkText, font=font, fill=shadowColor)
    #move down
    draw.text((x, y-adj), linkText, font=font, fill=shadowColor)
    #diagnal left up
    draw.text((x-adj, y+adj), linkText, font=font, fill=shadowColor)
    #diagnal right up
    draw.text((x+adj, y+adj), linkText, font=font, fill=shadowColor)
    #diagnal left down
    draw.text((x-adj, y-adj), linkText, font=font, fill=shadowColor)
    #diagnal right down
    draw.text((x+adj, y-adj), linkText, font=font, fill=shadowColor)
draw.text((x,y), linkText, font=font, fill=textColor)

img.save(output)
print 'Finished'
