
import json
import os

def parseAnnotations(path):
    '''
        Returns docs as a dictionary {paper_id, adju_relevance, 
        title, background_label, method_label, result_label, abstract}
    '''

    with open(path, 'r') as f:
        doc_json = {
            "paper_id": "",
            "adju_relevance": "",
            "title": "",
            "background_label": "",
            "method_label": "",
            "result_label": "",
            "abstract": ""
        }
        docs = []
        lines = f.readlines()
        lines.pop(0)
        while lines:
            line = lines.pop(0)
            # print(line)
            if line.startswith('paper_id:'):
                paper_id = line.split(';')[0].split(': ')[1].strip()
                doc_json["paper_id"] = paper_id
            elif line.startswith('TITLE:'):
                title = ': '.join(line.split(': ')[1:]).strip()
                doc_json["title"] = title
            elif line.startswith('ABSTRACT:'):
                abstract = ': '.join(line.split(': ')[1:]).strip()
                complete_abstract = ""
                labelF = 0
                for label in ["background_label", "method_label", "result_label"]:
                    if abstract.startswith(label):
                        abstract = ': '.join(abstract.split(': ')[1:]).strip()
                        doc_json[label] = doc_json[label] + ' ' + abstract
                        complete_abstract = complete_abstract + ' ' + abstract
                        labelF = 1
                        break
                if abstract.startswith('objective_label'):
                    abstract = ': '.join(abstract.split(': ')[1:]).strip()
                    doc_json['background_label'] = doc_json['background_label'] + ' ' + abstract
                    complete_abstract = complete_abstract + ' ' + abstract
                elif labelF == 0:
                    abstract = ': '.join(abstract.split(': ')[1:]).strip()
                    complete_abstract = complete_abstract + ' ' + abstract
                while lines:
                    line = lines.pop(0)
                    label_found = False
                    for label in ["background_label", "method_label", "result_label"]:
                        if line.startswith(label):
                            line = ': '.join(line.split(': ')[1:]).strip()
                            label_found = True
                            doc_json[label] = doc_json[label] + ' ' + line
                            complete_abstract = complete_abstract + ' ' + line
                            break
                    if label_found:
                        continue
                    else:
                        if line.startswith("="):
                            doc_json["abstract"] = complete_abstract
                            for label in ["background_label", "method_label", "result_label", "abstract"]:
                                if len(doc_json[label])!=0:
                                    doc_json[label] = doc_json[label][1:]

                            docs.append(doc_json)
                            doc_json = {
                                "paper_id": "",
                                "adju_relevance": "",
                                "title": "",
                                "background_label": "",
                                "method_label": "",
                                "result_label": "",
                                "abstract": ""
                            }
                            break
                        if line.startswith("objective_label"):
                            line = ': '.join(line.split(': ')[1:]).strip()
                            doc_json['background_label'] = doc_json['background_label'] + ' ' + line
                            complete_abstract = complete_abstract + ' ' + line
                        else:
                            line = ': '.join(line.split(': ')[1:]).strip()
                            complete_abstract = complete_abstract + ' ' + line

            elif line.startswith('adju relevance: '):
                # print(line)
                adju_relevance = line.split(': ')[1].split(' ')[1].split('(')[1].strip()
                doc_json["adju_relevance"] = adju_relevance[:-1]

            elif line.startswith('difference: ') or line.startswith('sources: '):
                continue

    if doc_json.get("paper_id") and doc_json["paper_id"]!='':
        docs.append(doc_json)
    
    return docs


# parseAnnotations('file.txt')

def main():
    
    input_dir = './readable_annotations/'
    output_dir = './parsed_annotations/'
    for file_name in os.listdir(input_dir):
        print(file_name)
        path = os.path.join(input_dir, file_name)
        docs = parseAnnotations(path)
        with open(os.path.join(output_dir, file_name.split('.')[0]+'.json'), 'w') as f:
            json.dump(docs, f)


if __name__ == "__main__":
    main()
