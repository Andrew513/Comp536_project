from datasets import load_dataset
class Simulator:
    def __init__(self):
        self.prompt_to_response = {
            "你好": ["你好，有什麼我可以幫忙的？"],
            "今天天氣如何？": ["今天天氣晴朗，溫度約 25 度。"]
        }
    def load_sharegpt(self, mode='single'):
        # Load the 'train' split directly so iteration yields examples, not split names
        dataset = load_dataset(
            "json",
            data_files={
                "train": "https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json"
            },
            split="train",
        )

        for entry in dataset:
            conv = entry['conversations']
            if mode == 'single' and len(conv) >= 2:
                user_prompt = conv[0]['value'].strip()
                assistant_response = conv[1]['value'].strip()
                self.prompt_to_response[user_prompt] = [assistant_response]
            elif mode == 'multi':
                for i in range(0, len(conv)-1, 2):
                    if conv[i]["from"] == "human" and conv[i+1]["from"] == "gpt":
                        self.prompt_to_response[conv[i]["value"].strip()] = [conv[i+1]["value"].strip()]

    def generate(self, request):
        """Accept either a raw prompt string or a SequenceGroup/Sequence object.

        Returns list[str] (one per seq), or a single-string (converted to list).
        """
        # raw prompt
        if isinstance(request, str):
            prompt = request
        else:
            prompt = None
            # common SequenceGroup attribute
            if hasattr(request, "prompt"):
                prompt = getattr(request, "prompt")
            # SequenceGroup usually has seqs list
            elif hasattr(request, "seqs") and len(request.seqs) > 0:
                seq = request.seqs[0]
                # try a few common places where prompt text may be stored
                if hasattr(seq, "data") and getattr(seq.data, "prompt_text", None):
                    prompt = seq.data.prompt_text
                elif getattr(seq, "prompt_text", None):
                    prompt = seq.prompt_text
            # fallback to request_id or empty string
            if prompt is None:
                prompt = getattr(request, "request_id", "")

        prompt = prompt.strip()
        # return from map, default fallback
        return self.prompt_to_response.get(prompt, ["這是模擬回答"])