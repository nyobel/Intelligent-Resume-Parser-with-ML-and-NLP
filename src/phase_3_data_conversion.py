import spacy
from spacy.tokens import DocBin
from phase_3_training_data import TRAINING_DATA
import random

# Create a blank English pipeline (no components)
nlp = spacy.blank("en")

def find_substring_span(text, substring):
    """
    Find the start and end indices of a substring within a text.
    Returns (start, end) or None if not found.
    """
    start = text.find(substring)
    if start == -1:
        return None
    end = start + len(substring)
    return start, end

def convert_data(data, filename):
    """
    Convert annotated training data to spaCy's binary DocBin format.
    Args:
        data: List of (text, annotations) tuples
        filename: Output file to save the DocBin object
    """
    doc_bin = DocBin()  # container for storing processed Doc objects
    accepted = 0
    rejected = 0

    for text, annot in data:
        try:
            doc = nlp.make_doc(text)
            ents = annot.get("entities")
            spans = []

            for start, end, label in ents:
                substring = text[start:end]
                corrected = find_substring_span(text, substring)
                if corrected:
                    start, end = corrected
                span = doc.char_span(start, end, label=label, alignment_mode="strict")
                if span is None:
                    span = doc.char_span(start, end, label=label, alignment_mode="contract")
                if span is None:
                    span = doc.char_span(start, end, label=label, alignment_mode="expand")

                if span is not None:
                    spans.append(span)
                else:
                    print(f"⚠ char_span failed for: '{text[start:end]}' in '{text}'")

            doc.ents = spans

            if len(doc.ents) != len(ents):
                raise ValueError("Some spans could not be aligned with tokens")

            doc_bin.add(doc)
            accepted += 1

        except Exception as e:
            print(f"❌ Rejected: {text}\n   Reason: {e}\n")
            rejected += 1

    doc_bin.to_disk(filename)
    print(f"✅ Saved {filename} with {accepted} records (Rejected: {rejected})")


if __name__ == "__main__":
    # Shuffle and split the data for training and development sets
    random.shuffle(TRAINING_DATA)
    split = int(len(TRAINING_DATA) * 0.8)
    train_data = TRAINING_DATA[:split]
    dev_data = TRAINING_DATA[split:]

    # Convert and save the datasets
    convert_data(train_data, "train.spacy")
    convert_data(dev_data, "dev.spacy")
