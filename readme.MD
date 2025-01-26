## Story Generator (powered by AI)

### **Premissas assumidas no projeto:**

1. **O usuário será colaborativo e fornecerá respostas válidas:**
   - Premissa: O usuário responderá às perguntas de forma compreensível e dentro do contexto (ex.: ao ser perguntado sobre "seu animal favorito", ele não deixará a resposta em branco ou responderá algo incoerente).
   - Risco: Não há validação para entradas inválidas ou em branco, o que pode levar a um comportamento inesperado.

2. **As variáveis de ambiente `API_KEY` e `LLM_MODEL` estarão corretamente configuradas:**
   - Premissa: O arquivo `.env` conterá valores válidos para as chaves de API do modelo (ex.: `API_KEY`) e o nome do modelo escolhido (ex.: `LLM_MODEL`).
   - Risco: Se essas variáveis não forem configuradas corretamente, o código pode falhar ao inicializar a API ou ao gerar a história.

3. **O modelo de linguagem escolhido (via `LLM_MODEL`) será compatível com a biblioteca utilizada (`Anthropic`):**
   - Premissa: O modelo configurado é compatível com os parâmetros do método `client.messages.create`, incluindo `max_tokens`, `temperature`, etc.
   - Risco: Escolher um modelo incorreto ou desatualizado pode causar erros na solicitação à API.

4. **O limite de `max_tokens` será suficiente para a resposta gerada:**
   - Premissa: O valor configurado (500 tokens) será adequado para gerar histórias completas com base nas respostas do usuário.
   - Risco: Se o modelo precisar de mais tokens para uma resposta coerente, a história pode ser truncada.

5. **O usuário terá acesso ao terminal para interagir com o script:**
   - Premissa: O usuário poderá executar o script em um ambiente que permita entrada e saída via terminal.
   - Risco: Em ambientes sem suporte para entrada interativa (ex.: interfaces web, contêineres sem TTY), o script não funcionará.

6. **A biblioteca `Anthropic` estará corretamente instalada e configurada:**
   - Premissa: A biblioteca utilizada para se comunicar com o modelo estará funcional no ambiente onde o código será executado.
   - Risco: Dependências desatualizadas ou ausentes podem gerar falhas na execução.

7. **A conexão com a API será estável durante a execução:**
   - Premissa: O sistema terá uma conexão de rede confiável para enviar solicitações à API da Anthropic.
   - Risco: Conexões instáveis podem causar erros ou atrasos no retorno da resposta.

8. **A história gerada será apropriada e consistente:**
   - Premissa: O modelo de IA utilizado criará histórias relevantes, criativas e coerentes, baseando-se nas respostas fornecidas pelo usuário.
   - Risco: O modelo pode gerar respostas incoerentes, ofensivas ou inadequadas se não for configurado ou usado corretamente.

9. **O usuário entende que o script tem fins recreativos:**
   - Premissa: O propósito principal do script é o entretenimento, e os resultados não têm impacto em decisões críticas.
   - Risco: Se o usuário esperar precisão ou seriedade, ele pode se frustrar com os resultados.

10. **As respostas do usuário estão no idioma esperado (Português):**
    - Premissa: Todas as perguntas e respostas estão em português, já que o script e o prompt estão adaptados para este idioma.
    - Risco: Se o usuário responder em outro idioma, a história pode não ser gerada adequadamente.

---

### **Limitações do Código**

1. **Ausência de validação de entrada do usuário:**
   - Atualmente, o código não verifica se o usuário fornece respostas válidas (ex.: entradas vazias, caracteres especiais ou respostas muito longas). Isso pode gerar histórias incoerentes ou erros no processo.

2. **Falta de tratamento de erros detalhado:**
   - Em caso de falha na comunicação com a API (ex.: problemas de rede, chave de API inválida, modelo indisponível), a mensagem de erro exibida ao usuário não é detalhada ou amigável.

3. **Histórias potencialmente truncadas:**
   - O limite de `500 tokens` para a geração de histórias pode ser insuficiente para criar uma narrativa completa e envolvente, especialmente se o modelo usar tokens para interpretar perguntas longas.

4. **Ausência de interface mais amigável:**
   - A interação com o terminal é simples, mas pode não ser atraente ou intuitiva para usuários que não estejam acostumados a utilizar linhas de comando.

5. **Dependência exclusiva do idioma português:**
   - O sistema presume que todas as perguntas e respostas serão feitas em português, o que limita sua aplicabilidade para usuários de outros idiomas.

6. **Personalização limitada da história:**
   - O modelo gera histórias com base apenas nas respostas do usuário, sem oferecer opções adicionais de personalização, como tom da narrativa, gênero da história, ou escolha de personagens.

7. **Falta de persistência ou histórico:**
   - O script não salva as respostas ou a história gerada. Caso o usuário queira reutilizar ou revisar as histórias, ele precisará executá-lo novamente.

8. **Dependência de um único modelo de IA:**
   - O código usa o modelo especificado em `LLM_MODEL`, mas não permite ao usuário escolher entre diferentes modelos ou ajustar configurações como temperatura ou número de tokens.

---

### **Possíveis Melhorias**

1. **Adicionar validação de entrada:**
   - Implementar verificações para garantir que o usuário forneça respostas válidas e significativas.

2. **Mensagens de erro mais amigáveis:**
   - Melhorar o tratamento de erros e exibir mensagens claras para o usuário quando algo der errado, como:
     - Problemas de conexão com a API.
     - Chave de API ausente ou inválida.
     - Limite de tokens excedido.

3. **Opções para personalização da história:**
   - Permitir que o usuário escolha o tom da narrativa (ex.: engraçado, dramático, inspirador) ou que inclua elementos adicionais na história, como personagens, época ou tema. Além disso, o usuário poderia escolher um estilo literário específico ou até mesmo um autor, para que a IA gerasse uma história parecida com o tipo de história que o autor criaria.

4. **Persistência de dados:**
   - As histórias, juntamente com as perguntas/respostas, poderiam ser armazenadas em um banco de dados. O produto poderia oferecer um acesso gratuito, exigindo cadastro, onde o usuário poderia gerar até 3 histórias mensalmente, sem armazenamento. Poderia existir também uma opção de assinatura, com geração ilimitada de histórias e armazenamento das histórias em um banco de dados. A partir do momento em que o usuário deixasse de ser assinante, ele perderia o acesso às histórias geradas por ele, porém elas continuariam armazenadas e poderiam voltar a ser acessadas através de uma nova assinatura.

5. **Suporte a múltiplos idiomas:**
   - Adaptar o sistema para funcionar em outros idiomas, detectando automaticamente o idioma das respostas ou permitindo que o usuário escolha antes de começar.

6. **Interface web:**
   - Implementar uma interface web para o produto, tornando a experiência do usuário mais intuitiva e atraente.

7. **Configurações ajustáveis para o modelo de IA:**
   - Permitir que o usuário ajuste parâmetros como:
     - Temperatura (criatividade).
     - Comprimento máximo da resposta.
     - Modelo de linguagem.

8. **Adicionar um modo de teste:**
   - Para facilitar o desenvolvimento, implementar um modo de teste que simula respostas do usuário sem interação manual.

9. **Implementar feedback do usuário:**
    - Após a geração da história, pedir que o usuário avalie a narrativa ou sugira ajustes para melhorias futuras.

10. **Personalizar perguntas:**
    - Atualmente as perguntas são fixas. Seria ótimo se o usuário conseguisse criar as próprias perguntas e também definir a quantidade de perguntas.

---

### **Decisões Arquiteturais e Justificativas**

<table style="width: 100%; border-collapse: collapse; margin: 20px 0; font-family: Arial, sans-serif;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 12px; background-color: #2c1f9e; font-weight: bold;">Camada</th>
      <th style="border: 1px solid #ddd; padding: 12px; background-color: #2c1f9e; font-weight: bold;">Tecnologias Propostas</th>
      <th style="border: 1px solid #ddd; padding: 12px; background-color: #2c1f9e; font-weight: bold;">Justificativa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 12px;">Frontend</td>
      <td style="border: 1px solid #ddd; padding: 12px;">React, TypeScript, TailwindCSS</td>
      <td style="border: 1px solid #ddd; padding: 12px;">React foi escolhido devido à sua maturidade, flexibilidade e amplo ecossistema de bibliotecas, o que facilita a criação de uma interface interativa e eficiente, essencial para experiências como canvas (Brand Zone). TypeScript melhora a manutenção e escalabilidade ao introduzir tipagem estática, reduzindo bugs. TailwindCSS acelera o desenvolvimento de UI com utilitários consistentes e design responsivo.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 12px;">Backend</td>
      <td style="border: 1px solid #ddd; padding: 12px;">Node.js, NestJS, REST</td>
      <td style="border: 1px solid #ddd; padding: 12px;">Node.js é altamente performático e escalável, ideal para lidar com operações assíncronas e requisitos em tempo real. NestJS adiciona uma estrutura modular baseada em TypeScript, permitindo a criação de um backend organizado e escalável, com suporte a práticas RESTful padrão. REST foi escolhido pela simplicidade na integração com o frontend e pela ampla adoção em APIs públicas, permitindo maior interoperabilidade com ferramentas e bibliotecas existentes. Além disso, ele facilita a documentação e a compatibilidade com clientes que não usam GraphQL.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 12px;">Módulo de IA</td>
      <td style="border: 1px solid #ddd; padding: 12px;">Stable Diffusion</td>
      <td style="border: 1px solid #ddd; padding: 12px;">Stable Diffusion é uma solução avançada e personalizável para geração de imagens, permitindo controle sobre o estilo e alinhamento com as diretrizes de marca definidas no Brand Zone. Sua flexibilidade permite ajustes finos para manter consistência com identidades visuais específicas. É amplamente utilizado em aplicações criativas e oferece suporte robusto para uso local ou em infraestrutura cloud.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 12px;">Banco de Dados</td>
      <td style="border: 1px solid #ddd; padding: 12px;">PostgreSQL</td>
      <td style="border: 1px solid #ddd; padding: 12px;">PostgreSQL é altamente confiável, com suporte avançado para operações complexas, incluindo índices robustos e consultas avançadas para grandes volumes de dados estruturados (diretrizes de marca e histórico de assets). Seu suporte nativo a tipos de dados JSON facilita o armazenamento de configurações semiestruturadas, como personalizações de identidade visual.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 12px;">Infraestrutura</td>
      <td style="border: 1px solid #ddd; padding: 12px;">GCP (Cloud Run, Cloud Storage, Cloud SQL, Pub/Sub, Cloud CDN, Load Balancer, API Gateway)</td>
      <td style="border: 1px solid #ddd; padding: 12px;">Cloud Run é ideal para executar serviços baseados em contêiner de forma escalável e gerenciada, reduzindo a necessidade de administração de servidores. O Load Balancer assegura a distribuição eficiente de tráfego entre as instâncias do Cloud Run, garantindo alta disponibilidade e menor tempo de resposta. O API Gateway protege as comunicações entre o Frontend e o Backend, oferecendo autenticação, limitação de taxa (rate limiting) e gerenciamento de segurança centralizado. Cloud SQL gerencia o banco de dados com alta disponibilidade e backups automáticos. Pub/Sub é essencial para filas assíncronas de processamento, como a geração de imagens. Cloud CDN garante entrega rápida e eficiente de assets visuais, enquanto o Cloud Storage é ideal para armazenar assets com segurança e eficiência.</td>
    </tr>
  </tbody>
</table>
