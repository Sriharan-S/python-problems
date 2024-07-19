import markdown
import os
def convert_markdown_to_html(markdown_file_path, html_file_path):
    """Convert a Markdown file to an HTML file."""
    try:
        with open(markdown_file_path, 'r') as md_file:
            markdown_text = md_file.read()
        html_text = markdown.markdown(markdown_text)
        with open(html_file_path, 'w') as html_file:
            html_file.write(html_text)

        print(f"Markdown file '{markdown_file_path}' has been converted to HTML file '{html_file_path}'.")

    except FileNotFoundError:
        print(f"File not found: {markdown_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
markdown_file_path = 'example.md'  
html_file_path = 'output.html' 
convert_markdown_to_html(markdown_file_path, html_file_path)
