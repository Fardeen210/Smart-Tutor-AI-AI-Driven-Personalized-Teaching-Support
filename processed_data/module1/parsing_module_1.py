from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader

# set up parser
parser = LlamaParse(
    result_type="markdown",
    extract_layout=True,
    disable_image_extraction=True,
    page_separator="\n== {pageNumber} ==\n" 
)

# use SimpleDirectoryReader to parse our file
documents = SimpleDirectoryReader(input_files=['data\Module_1\INFO5731_Syllabus_Sping2025_updated_01142025.pdf']).load_data()

print(documents)


