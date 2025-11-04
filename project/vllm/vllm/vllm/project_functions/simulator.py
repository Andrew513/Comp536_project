class Simulator:
    def __init__(self):
        self.prompt_to_response = {
            "你好": ["你好，有什麼我可以幫忙的？"],
            "今天天氣如何？": ["今天天氣晴朗，溫度約 25 度。"]
        }

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

        # return from map, default fallback
        return self.prompt_to_response.get(prompt, ["這是模擬回答"])