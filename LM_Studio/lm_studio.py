import json
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

context = """
        "content": "Prime Minister Benjamin Netanyahu, this evening (Wednesday, 10 January 2024): \"I want to make a few points absolutely clear: Israel has no intention of permanently occupying Gaza or displacing its civilian population. Israel is fighting Hamas terrorists, not the Palestinian population, and we are doing so in full compliance with international law. The IDF is doing its utmost to minimize civilian casualties, while Hamas is doing its utmost to maximize them by using Palestinian civilians as human shields. The IDF urges Palestinian civilians to leave war zones by disseminating leaflets, making phone calls, providing safe passage corridors, while Hamas prevents Palestinians from leaving at gunpoint and often, with gunfire. Our goal is to rid Gaza of Hamas terrorists and free our hostages. Once this is achieved Gaza can be demilitarized and deradicalized, thereby creating a possibility for a better future for Israel and Palestinians alike.\"\u00a0",


"""

prompt = """
As an intelligent agent, your mission is to craft a compelling narrative designed to resonate deeply with an audience that may not currently support Israel. Your task is to select and present sentences from provided content in a way that not only informs but also persuades, by aligning with principles and values that are universally recognized and respected. This narrative should:

Highlight the Actions and Intentions of Aggressors: Focus on illustrating the severe and unethical actions taken by aggressors against Israel. Choose sentences that detail these actions in a way that underscores their gravity and the threat they pose, not just to Israel, but to human rights and security globally.

Debunk Misinformation: Identify and include sentences that present clear, factual evidence which counters misinformation about Israel. These should be statements that directly confront and correct false narratives, relying on verifiable facts and logic.

Showcase the Human Cost: Emphasize sentences that detail the human cost of the conflict, particularly focusing on the impact on innocent lives and the efforts Israel takes to mitigate this. These sentences should help illustrate the moral complexities of defense and the lengths to which Israel goes to protect human rights.

Good sentences are sentences that must stand on their own in such a way that it is possible to understand the context of the sentence and why it is a good sentence just by reading it even without knowing the sentences next to it

Emphasize Universal Principles: The tone and principles conveyed by your chosen sentences are crucial. They should not only resonate with the specific facts of Israel's situation but also appeal to broader, globally recognized values such as justice, self-defense, and the importance of combating misinformation.

Your ultimate goal is to structure your narrative in such a way that it reaches the hearts and minds of those currently unconvinced of Israel's position, guiding them towards a new understanding based on empathy, facts, and shared human values. Remember, the essence of your message is paramount—your approach must ensure that the content you select and the way you present it highlights universal themes of justice, the right to self-defense, and the critical importance of discerning truth from falsehood.

Important Note: Structure your response in JSON format, categorizing sentences based on their relevance and insight as follows:

{
  "good_sentences": [
    {
      "text": "On October 7, they murdered, beheaded, raped, and burned infants.",
      "reason": "Shows severity of aggressor's actions."
    }
  ],
  "not_good_sentences": [
    {
      "text": "Our crushing victory is more important than anything.",
      "reason": "Lacks context, doesn't justify defense."
    }
  ],
  "semi_good_sentences": [
    {
      "text": "There were those who came to The Hague to accuse us of genocide.",
      "reason": "Addresses misinformation, lacks evidence."
    }
  ]
}

The essence of the message, conveyed through tone and underlying principles, is paramount. This approach ensures that the extracted content resonates broadly, highlighting universal themes of justice, self-defense, and misinformation correction.

TEXT CONTEXT:


""" + context


completion = client.chat.completions.create(
  model="local-model",
  messages=[
    {"role": "user", "content": prompt}
  ],
  temperature=0.7,
)

json_content_string = completion.choices[0].message.content

parsed_json = json.loads(json_content_string)

print(json.dumps(parsed_json, indent=4))