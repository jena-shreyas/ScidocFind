import os
import json

def parseAnnotations(path):
    '''
        Returns docs as a dictionary {paper_id, adju_relevance, 
        title, background_label, method_label, result_label, abstract}
    '''
    with open(path, 'r') as f:
        doc_json = {}
        docs = []
        lines = f.readlines()
        lines.pop(0)
        while lines:
            line = lines.pop(0)
            if line.startswith('paper_id:'):
                paper_id = line.split(';')[0].split(': ')[1].strip()
                doc_json["paper_id"] = paper_id
            elif line.startswith('TITLE:'):
                title = ': '.join(line.split(': ')[1:]).strip()
                doc_json["title"] = title
            elif line.startswith('ABSTRACT:'):
                abstract = ': '.join(line.split(': ')[1:]).strip()
                complete_abstract = ""
                for label in ["background_label", "method_label", "result_label"]:
                    if abstract.startswith(label):
                        abstract = ': '.join(abstract.split(': ')[1:]).strip()
                        if doc_json.get(label):
                            doc_json[label] = doc_json[label] + ' ' + abstract
                            complete_abstract = doc_json[label]
                        else:
                            doc_json[label] = abstract
                            complete_abstract = abstract
                        break
                while lines:
                    line = lines.pop(0)
                    label_found = False
                    for label in ["background_label", "method_label", "result_label"]:
                        if line.startswith(label):
                            line = ': '.join(line.split(': ')[1:]).strip()
                            label_found = True
                            if doc_json.get(label):
                                doc_json[label] = doc_json[label] + ' ' + line
                                complete_abstract = complete_abstract + \
                                    ' ' + doc_json[label]
                            else:
                                doc_json[label] = line
                                complete_abstract = complete_abstract+' '+line
                            break
                    if label_found:
                        continue
                    else:
                        doc_json["abstract"] = complete_abstract
                        docs.append(doc_json)
                        doc_json = {}
                        break

            elif line.startswith('adju relevance: '):
              try:
                adju_relevance = line.split(': ')[1].split(' ')[1].split('(+')[1].strip()
                doc_json["adju_relevance"] = int(adju_relevance[:-1])
              except IndexError:
                adju_relevance = line.split(': ')[1].split(' ')[1].split('(')[1].strip()
                doc_json["adju_relevance"] = int(adju_relevance[:-1])
            elif line.startswith('difference: ') or line.startswith('sources: '):
                continue

    if doc_json.get("paper_id"):
        docs.append(doc_json)
    return docs


if __name__=='__main__':
    dir_path = 'CSFCube/readable_annotations/'
    output_dir_path = 'parsed_annotations/'
    annotations = dict()
    all_files  = os.listdir(dir_path)
    filenames = [file for file in all_files if os.path.isfile(os.path.join(dir_path, file))]
    for filename in filenames:
        annotations = parseAnnotations(dir_path + filename)
        output_file = output_dir_path + filename.split('.txt')[0] + '.json'
        with open(output_file, 'w') as f:
            json.dump(annotations, f)

        # with open(output_file, 'r') as f:
        #     annot = json.load(f)
        #     for paper_dict in annot:
        #         print(paper_dict.keys())
            