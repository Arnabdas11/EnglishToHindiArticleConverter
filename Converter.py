
# Converting the English text into Hindi text using the Facebook M2M-418m model
# Converting it by line by line and then later adding them up
def converter(text, pipe):
    result = []
    for i in range(len(text)):
        hindi = pipe(text[i], forced_bos_token_id=pipe.tokenizer.get_lang_id(lang='hi'))
        h = hindi[0].get('generated_text')
        result.append(h)
    return result


# Sentencing the text based on end of sentence. It helps in converting the text from English to Hindi
def sentencing(text):
    sentenced_text = []
    pos = 0
    while pos != -1:
        pos = text.find(". ")
        lst = text[:pos]
        text = text[pos + 1:]
        sentenced_text.append(lst)
    return sentenced_text

# # These are experimental codes
# def text_extractor(df):
#     my_list = []
#     for i in range(df['block_num'].nunique()):
#         a = df[df['block_num'] == i+1]['text']
#         b = a.to_list()
#         object_string = ' '.join([str(x) for x in b])
#         my_list.append(object_string)
#     return my_list

# def prep_text(file):
#     df = pd.read_csv(file)
#     df = df[df['conf'] > 0]
#     df.reset_index(inplace=True, drop=True)
#     my_list = text_extractor(df)
#     text = []
#     for ele in my_list:
#         if ele.strip():
#             text.append(ele)
#     return text