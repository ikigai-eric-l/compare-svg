#!/usr/bin/env python3
"""
Simplify SVG by removing special attributes except basic colors and gradients
"""
import re
import sys

def simplify_svg(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove filters
    content = re.sub(r'<filter[^>]*>.*?</filter>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*filter="[^"]*"', '', content)

    # Remove masks but keep the content inside
    content = re.sub(r'<mask[^>]*>.*?</mask>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*mask="[^"]*"', '', content)

    # Remove clip-paths but keep the content inside
    content = re.sub(r'<clipPath[^>]*>.*?</clipPath>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*clip-path="[^"]*"', '', content)

    # Remove opacity attributes
    content = re.sub(r'\s*opacity="[^"]*"', '', content)
    content = re.sub(r'\s*fill-opacity="[^"]*"', '', content)
    content = re.sub(r'\s*stroke-opacity="[^"]*"', '', content)

    # Remove transform attributes (except in gradient definitions)
    content = re.sub(r'(<(?!linearGradient|radialGradient)[^>]*)\s*transform="[^"]*"', r'\1', content)

    # Remove style attributes except basic ones
    content = re.sub(r'\s*style="[^"]*"', '', content)

    # Remove empty groups
    content = re.sub(r'<g>\s*</g>', '', content)
    content = re.sub(r'<g\s+/>', '', content)

    # Clean up extra whitespace and newlines
    content = re.sub(r'\n\s*\n', '\n', content)
    content = re.sub(r'  +', ' ', content)

    # Keep only basic SVG structure with paths, rects, and gradients
    # This preserves fill colors and gradient definitions

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(open(input_file, 'rb').read()), len(open(output_file, 'rb').read())

if __name__ == '__main__':
    original_size, simplified_size = simplify_svg('grid.svg', 'grid-simplified.svg')
    print(f'Original: {original_size:,} bytes')
    print(f'Simplified: {simplified_size:,} bytes')
    print(f'Reduction: {(1 - simplified_size/original_size)*100:.1f}%')
