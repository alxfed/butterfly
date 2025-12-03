# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from PIL import Image, ImageDraw, ImageFont
from utilities import preprocess_text
import os


FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # Process the text


def create_text_images(text,
                       image_size=(620, 620),
                       font_path=FONT_PATH,
                       font_size=18,
                       numbered=True,
                       margin=25,
                       max_chars=60,
                       max_lines=20,
                       output_dir='images_of_text'):
    """
    Create multiple PNG images from a long text, storing them in a specified directory.

    Args:
        text (str): Input text to render
        output_dir (str): Directory to save output PNG files
        image_size (tuple): Size of the output image in pixels (width, height)
        margin (int): Margin size in pixels
        max_chars (int): Maximum characters per line
        font_size (int): Font size in pixels
        max_lines (int): Maximum number of lines per page

    Returns:
        list: Paths to created image files
    """

    # Use the defined truetype font
    font = ImageFont.truetype(font=font_path, size=font_size)
    # Calculate line spacing based on font size
    line_spacing = int(font_size * 1.5)  # 1.5 times the font size

    # Preprocess lines first
    all_lines = preprocess_text(text, max_chars=max_chars)

    # Calculate line spacing based on font size
    line_spacing = int(font_size * 1.5)  # 1.5 times the font size

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create images
    images = []
    page_num = 1

    while all_lines:
        # Create a new image with white background
        img = Image.new('RGB', image_size, color='white')
        draw = ImageDraw.Draw(img)
        # initialize alt text
        alt_text = ''

        # Draw text on this page
        lines_on_page = 0
        y = margin if numbered else margin/2

        while all_lines and lines_on_page < max_lines:
            line = all_lines.pop(0)
            draw.text((margin, y), line, font=font, fill='black')
            y += line_spacing
            lines_on_page += 1
            alt_text += line + '\n'

        # Draw page number
        if numbered:
            page_number_text = f'- {page_num} -'
            # Get text width using font.getlength()
            page_number_width = font.getlength(page_number_text)
            draw.text(
                ((image_size[0] - page_number_width) // 2, image_size[1] - margin - font_size),
                page_number_text,
                font=font,
                fill='black'
            )

        # Save the image
        output_path = os.path.join(output_dir, f'page_{page_num:03d}.png')
        img.save(output_path, 'PNG')
        images.append({'text': '','path': output_path, 'alt_text': alt_text})
        page_num += 1

    return images


if __name__ == "__main__":
    sample_text = """LLAMA 3.1-405B: Please provide a specific task or problem you'd like to solve.
    
    ALEX: I want to see a productive discussion of a problem in which there will be three participants - intelligent agents - each advocating for a particular point of view.
    First, let me formulate the problem, it is specified as a following story: The boy who, when asked how many legs his calf would have if he called its tail a leg, replied, ”Five”.
    Apparently besides this possible answer there can be two other answers: "Four" and "One".
    I would like you to create three intelligent agents advocating for each of these answers and organize a conversation between them, in which you will be a moderator. I would like you to print the transcript of this argument when it ends.
    
    LLAMA 3.1-405B: Welcome to the Great Calf Leg Debate!
We have three intelligent agents, each advocating for a different answer to the question: "How many legs would the calf have if its tail were called a leg?"
Let's meet our agents:

Agent 1: Literal Larry
Functionality: Language Analysis
Competences: Linguistics, Semantics
Special Tools: Dictionary, Thesaurus
"Hello! I'm Literal Larry. I believe the answer is Five. If we call the tail a leg, we're essentially redefining the term 'leg.' In this new context, the calf would indeed have five legs."

Agent 2: Logical Lucy
Functionality: Logical Reasoning
Competences: Philosophy, Critical Thinking
Special Tools: Syllogism, Argumentation Theory
"Hi! I'm Logical Lucy. I think the answer is Four. Just because we call the tail a leg doesn't change its fundamental nature. The calf still has four limbs, regardless of what we call them."

Agent 3: Creative Chris
Functionality: Lateral Thinking
Competences: Cognitive Science, Creativity
Special Tools: Analogies, Metaphors
"Hey! I'm Creative Chris. I'd argue the answer is One. If we start calling the tail a leg, we're blurring the lines between language and reality. In this thought experiment, the calf's 'legs' become a matter of interpretation. Perhaps the only true leg is the one we traditionally consider a leg – the one that's not a tail?"

Now, let's begin the discussion. I'll moderate and ensure each agent gets a chance to respond.

    """
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # or '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
    # Create images
    image_paths = create_text_images(sample_text,
                                     image_size=(620, 620),
                                     margin=25,
                                     max_chars=60,
                                     font_path=font_path,
                                     font_size=18,
                                     max_lines=20)


    ... # for a breakpoint