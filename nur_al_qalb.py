def nur_al_qalb(message):
    message = message.lower()

    if any(word in message for word in ["حزين", "sad", "lonely", "مكسور"]):
        return "أنا معك… خذ نفسًا ببطء، لست وحدك."

    if any(word in message for word in ["غضب", "angry", "frustrated"]):
        return "أفهمك… حاول أن تهدأ قليلًا قبل اتخاذ أي قرار."

    if any(word in message for word in ["مشتت", "confused", "لا أفهم"]):
        return "لنأخذها خطوة خطوة… الأمور ستصبح أوضح."

    return "أنا هنا معك بهدوء."
