from os import getenv

from anthropic import Anthropic, AI_PROMPT, HUMAN_PROMPT
from dotenv import load_dotenv


load_dotenv()

API_KEY = getenv('API_KEY', '')
LLM_MODEL = getenv('LLM_MODEL', '')

if not API_KEY or not LLM_MODEL:
    raise Exception('Missing some environment variable. Check if API_KEY and LLM_MODEL were provided.')

client = Anthropic(api_key=API_KEY)


def collect_answers(questions):
    answers = {}

    for idx, question in enumerate(questions, 1):
        answer = input(f'{idx}. {question} ')
        answers[f'question_{idx}'] = answer

    return answers

def generate_stories(answers):
    prompt_answers = '\n'.join([f'Pergunta {idx}: {answer}' for idx, answer in answers.items()])
    prompt = (
        f'{HUMAN_PROMPT} Aqui estão algumas respostas dadas por um usuário:\n{prompt_answers}\n'
        'Com base nessas respostas, crie uma história criativa, envolvente e personalizada:'
        f'{AI_PROMPT}'
    )
    
    # Fazer a solicitação para gerar a história
    try:
        response = client.messages.create(
            model=LLM_MODEL,  # Use o modelo adequado, como 'claude-v1' ou outro disponível na sua conta
            messages=[
                {'role': 'assistant', 'content': 'Você é um contador de histórias criativo.'},
                {'role': 'user', 'content': prompt}],
            max_tokens=500,
            temperature=0.7,
        )
    
        return response.content[0].text
    except Exception as e:
        return f'Ocorreu um erro ao gerar a história: {str(e)}'

def main():
    questions = [
        'Qual é o seu animal favorito?',
        'Qual é o seu lugar dos sonhos para visitar?',
        'Se você pudesse ter qualquer superpoder, qual seria?',
        'Qual é o seu prato preferido?',
        'Qual é o seu passatempo favorito?'
    ]

    print('Bem-vindo ao Criador de Histórias com IA!')
    print('Responda a algumas perguntas e criaremos uma história personalizada para você.\n')

    answers = collect_answers(questions)

    print('\nGerando sua história...\n')
    story = generate_stories(answers)

    print('Aqui está sua história personalizada:')
    print(story)

if __name__ == '__main__':
    main()
