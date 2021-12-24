from sentence_transformers import SentenceTransformer
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
import pandas as pd
train = pd.read_csv('./train_samples.csv')
test = pd.read_csv('./test_samples.csv')
def cut_sentences(content):   # 实现分句的函数，content参数是传入的文本字符串
    end_flag = ['?', '!', '.', '？', '！', '。']   # 结束符号，包含中文和英文的
    content_len = len(content)
    sentences = []   # 存储每一个句子的列表
    tmp_char = ''
    for idx, char in enumerate(content):
        tmp_char += char   # 拼接字符
        if (idx + 1) == content_len:   # 判断是否已经到了最后一位
            sentences.append(tmp_char.strip().replace('\ufeff', ''))
            break
        if char in end_flag:   # 判断此字符是否为结束符号
            # 再判断下一个字符是否为结束符号，如果不是结束符号，则切分句子
            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char.strip().replace('\ufeff', ''))
                tmp_char = ''
              
    return sentences   # 函数返回一个包含分割后的每一个完整句子的列表
rr = '工业文明，是指工业社会文明亦即未来学家托夫勒所言的第二次浪潮文明，它贯穿着劳动方式最优化、劳动分工精细化、劳动节奏同步化、劳动组织集中化、生产规模化和经济集权化等六大基本原则。 工业文明学术解释 编辑 语音 工业文明是以工业化为重要标志、机械化大生产占主导地位的一种现代社会文明状态。其主要特点大致表现为工业化、城市化、法制化与民主化、社会阶层流动性增强、教育普及、消息传递加速、非农业人口比例大幅度增长、经济持续增长等。这些特征也可视作推动传统农耕文明向工业文明转轨的重要因素。 工业文明简介 编辑 语音 工业文明现阶段 迄今为止，工业文明是最富活力和创造性的文明。工业文明的优势是规模化生产使人类商品迅速丰富，缺陷是对地球资源的消耗与污染也急剧加速，21世纪的后工业化时代将进入可持续发展的循环经济、生态经济的高科技经济模式。工业社会是唯一的一个依赖持续的经济增长而生存的社会。财富的增长一旦停滞，工业社会就丧失了合法性。由财富的不断增长所要求，工业社会离不开创新，创新是工业社会生死攸关的基础。由创新所要求，工业社会中的知识增长也是无止境的。'
# sentence = cut_sentences(rr)
sentence = train['text'][:1]
print(sentence)



sentence_embeddings = model.encode(sentence)

for sentence, embedding in zip(sentence, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")