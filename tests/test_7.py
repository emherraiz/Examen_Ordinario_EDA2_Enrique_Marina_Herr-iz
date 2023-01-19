import huffman

def test_compress():
    freq_table = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15}
    root = huffman.build_huffman_tree(freq_table)
    code_table = {}
    huffman.build_code_table(root, "", code_table)
    message = "AF13M3T"
    compressed_message = huffman.compress(message, code_table)
    assert compressed_message == "1000110011"

def test_decompress():
    freq_table = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15}
    root = huffman.build_huffman_tree(freq_table)
    compressed_message = "1000110011"
    decompressed_message = huffman.decompress(compressed_message, root)
    assert decompressed_message == "AF13M3T"
