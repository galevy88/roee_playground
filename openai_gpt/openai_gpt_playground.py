
import json
from openai import OpenAI

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
        "content": "The following has been cleared for publication: Orders from the organization leadership, acquisition of UAVs and use of criminal elements: This is how Hamas terrorist organization senior operatives advanced attacks against innocents around the world. The Hamas terrorist organization is working to advance attacks against targets in the Middle East, Africa and Europe under the command of senior organization leaders. On 14 December 2023, the Danish and German security and enforcement authorities announced the widespread arrest of suspects in Europe who are now the subject of judicial proceedings. In a continuing intelligence effort, considerable information has been uncovered that proves how the Hamas terrorist organization has acted to expand its violent activity abroad in order to attack innocents around the world. Thanks to combined inter-organizational forces in Israel and abroad, a comprehensive and in-depth picture of Hamas's terrorist activities has been revealed, including details of areas of action, targets for attacks and those involved in implementing the activity \u2013 from Hamas commanders in Lebanon to the last attackers in the operational infrastructure, as well as information on the intention to attack the Israeli Embassy in Sweden, the acquisition of UAVs and the use of elements from criminal organizations in Europe. Hamas draws inspiration from the terrorist activity of the Iranian regime, and like it, aspires to attack Israeli, Jewish and Western targets at any price. The Mossad, the ISA and the IDF, in conjunction with the international security and enforcement bodies, will continue their efforts to thwart the terrorist intentions of Hamas and all terrorist organizations, and to settle accounts with them everywhere in the world, on behalf of the security of the State of Israel and the Jewish people. \u00a0",

"""

key = "ask-gal"
client = OpenAI(
    api_key=key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4",
)

json_content_string = chat_completion.choices[0].message.content

parsed_json = json.loads(json_content_string)

print(json.dumps(parsed_json, indent=4))
