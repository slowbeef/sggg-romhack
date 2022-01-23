# STORY01.MES

MES Files contain text in dialogue boxes like in the screenshots below. The Japanese text itself is Shift-JIS, with the “@” symbol signifying a control token. For example, in the simplest case, “@n” denotes a newline.

The MES files - like a lot of others in the GDI - follow a format where the files starts with offsets. These are absolute and in big-Endian byte format. And there can be repeats. The offsets represent the start of each dialogue box text.

For example:

![Story header hex](pics/story%20header%20hex.png)

STORY01.MES starts with “60 00 00 00”, meaning that the first text entry starts at 0x60 in the file. There’s a repeat “60 00 00 00” (not sure why) and then “58 06 00 00” which denotes the next text to parse starts at 0x0658.

This is fairly self explanatory - the text itself starts with some control codes, then it’s Shift-JIS. You can insert them directly and it doesn’t seem to break anything, but of course, SGGG is using Full-Width Font so just putting in English will be ugly as sin and you’ll run out of room fast.

The accompanying Python I wrote “sggg_story_extract.py” is fairly self-explanatory, but hopefully this provides additional context.
