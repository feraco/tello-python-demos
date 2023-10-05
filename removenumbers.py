{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
import re\
\
def remove_numbers_from_filename(directory_path):\
    # Get all files in the directory\
    for filename in os.listdir(directory_path):\
        # Create a new filename by removing all digits\
        new_filename = re.sub(r'\\d', '', filename)\
        \
        # Only rename if the filename has changed\
        if new_filename != filename:\
            old_file_path = os.path.join(directory_path, filename)\
            new_file_path = os.path.join(directory_path, new_filename)\
            \
            # Ensure not to overwrite an existing file\
            if not os.path.exists(new_file_path):\
                os.rename(old_file_path, new_file_path)\
                print(f"Renamed: \{filename\} -> \{new_filename\}")\
            else:\
                print(f"Skipped: \{filename\} (conflict with existing file)")\
\
# Example usage: replace the path in the next line\
remove_numbers_from_filename('/Users/wwhs-research/Downloads/UPH_DJITello-main/Chapter3FlyingPath')\
}