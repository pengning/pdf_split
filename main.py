import gradio as gr
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(filename, start_page, end_page):
    # 打开要分割的pdf文件

    with open(filename.name, 'rb') as infile:
        reader = PdfReader(infile)

        num_pages = len(reader.pages)
        # 检查用户输入的页码是否在范围内
        start_page = int(start_page)
        end_page = int(end_page)
        if start_page < 1:
            start_page = 1
        if end_page > num_pages:
            end_page = num_pages

        writer = PdfWriter()
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])
        # 拆分后的文件名为filename的前缀加上序号，例如：filename-1.pdf
        # output_filename = f"{filename[:-4]}-{start_page}.pdf"
        output_filename = f"out-{start_page}.pdf"
        with open(output_filename, 'wb') as outfile:
            writer.write(outfile)

    return output_filename


with gr.Blocks() as demo:
    gr.Markdown("# PDF_splitter")
    with gr.Tab("PDF分割"):
        pdf_input = gr.File(label="pdf输入")
        start_page= gr.Textbox(label="起始页")
        end_page = gr.Textbox(label="结束页")
        pdf_output = gr.File(label="pdf输出")
        file_button = gr.Button("分割PDF")

        file_button.click(split_pdf, inputs=[pdf_input,start_page,end_page], outputs=pdf_output)


demo.launch(share=True)