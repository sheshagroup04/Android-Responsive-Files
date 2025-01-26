
# Responsive App Source

This repo contains the java and python file to your app Responsive. It has java file to create dimen files and python file for creating the image of different dimensions. All are based in the mentioned file and their type as per Android Guide Lines

## How To Use
### Generate the Dp values
1. Run the File `Main.java`
2. Enter the value by which you have to multiply the normal Dp value. Example: 2.5 for values-sw800

### Generate the Sp values
1. Run the File `Font.java`
2. Enter the value by which you have to multiply the normal Sp value. Example: 2.5 for values-sw800

### Generate the Responsive Image
1. Run the cmd 
``` bash
pip install --upgrade pillow
```
2. Run the file main.py
3. A window will open select the image you want to resize or make it responsive
4. A window will open again select the location where you have to save the created responsive images
5. Now go the location and you will find the following folders (ldpi, hdpi, xhdpi, xxhdpi, xxxhdpi)
6. These folder are according to the Drawable folder in Android Studio

### There are some pre created dims file wich you can directly import in your android project. You will find them all in `dimens` folder


