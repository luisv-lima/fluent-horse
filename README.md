# 🐎 Fluent Horse

<img src="https://github.com/user-attachments/assets/47584933-44c6-4afd-8ec1-c8b30db778b9" width="800" alt="Fluent Horse Dashboard" />


**Fluent Horse** é uma plataforma inovadora (MVP) desenhada para revolucionar a forma como autodidatas estudam idiomas. O projeto integra curadoria automatizada de notícias, inteligência artificial e o método de *Spaced Repetition* (Repetição Espaçada) para oferecer um aprendizado contextual e dinâmico.
[![Acessar MVP](https://img.shields.io/badge/🚀_Acessar_o_App-Fluent_Horse-2ea44f?style=for-the-badge)](https://fluent-horse-ai.lovable.app/)
---

## 🎯 1. O Problema

Estudantes de inglês, especialmente autodidatas de nível básico ao intermediário, frequentemente sofrem com o "vácuo de contexto".
*   **A dor:** Métodos tradicionais focam em gramática isolada ou vocabulário genérico (ex: "The book is on the table").
*   **O impacto:** Isso torna extremamente difícil e frustrante para o aluno consumir conteúdos reais do dia a dia, como notícias internacionais, documentações técnicas ou artigos de negócios. A falta de conexão com a realidade leva ao desengajamento e ao abandono do estudo.

## 💡 2. A Ideia do Produto

Para combater o vácuo de contexto, o Fluent Horse propõe o aprendizado através da realidade:
*   **Curadoria Automatizada:** Um robô em Python varre diariamente sites de notícias (ex: BBC News) em busca de conteúdos relevantes nas categorias Mundo, Tecnologia e Esportes.
*   **Extração Inteligente (IA):** A API do Google Gemini analisa as notícias e extrai, traduz e explica os termos e frases mais importantes, gerando *flashcards* (cartões de estudo) prontos para uso.
*   **Retenção Científica:** A plataforma (construída em React) utiliza um sistema de repetição espaçada para garantir que o vocabulário das notícias seja memorizado a longo prazo.

## 📱 3. O Protótipo Criado

O MVP foi prototipado utilizando a ferramenta **Lovable** (com integração Supabase para banco de dados) e validado com um frontend responsivo em React e Tailwind CSS.

**Principais Funcionalidades do MVP:**
*   **Dashboard Personalizado:** Visão geral do progresso e acesso rápido a sessões de estudo.
*   **Daily News:** Feed de notícias reais transformadas em *decks* de estudo.
*   **Estudo Temático:** Opção para estudo focado (ex: Viagem, Tecnologia, Saúde).
*   **Criação de Decks:** Interface intuitiva que permite ao usuário colar suas próprias listas de vocabulário e gerar flashcards instantaneamente.
*   **Sistema de Flashcards:** Interface de estudo baseada em feedback de dificuldade (Fácil, Médio, Difícil).

## 🧪 4. O Experimento Realizado

Para testar as hipóteses do produto, foi conduzido um experimento focado em demonstração direta do protótipo e coleta de feedback qualitativo.

*   **Público do Experimento:** 5 indivíduos (incluindo usuários finais e a visão de desenvolvimento).
*   **Metodologia:** Demonstração do fluxo principal (ler uma notícia -> praticar os flashcards -> criar um deck próprio) seguida de um formulário estruturado de percepção de valor e usabilidade.

## 📊 5. Resultados da Validação

A análise dos feedbacks trouxe insights cruciais para o futuro do produto:

*   **Validação da Usabilidade:** Todos os usuários classificaram a plataforma como "Fácil" ou "Muito fácil" de usar. A interface *Clean* (Glassmorphism) ajudou a reduzir a carga cognitiva, comum em aplicativos de estudo complexos.
*   **Validação da Proposta de Valor:** Houve grande entusiasmo (ex: *"Adorei a ideia de estudar com notícias reais!"*) em relação ao aprendizado contextual. O recurso "Crie seu Deck", com exemplos visuais, foi apontado como um grande facilitador.
*   **Descobertas Técnicas:** O teste evidenciou um *bug* na ferramenta de Assistente de IA para geração avulsa de cards (um erro de processamento de texto que será corrigido), reforçando a necessidade de testes contínuos antes do lançamento oficial.
*   **Melhorias de UX Identificadas:** A necessidade de refinar o fluxo pós-leitura (adicionar um botão "Praticar Agora" nas notícias) e alterar a nomenclatura técnica de "Baralhos" para "Cards" ou "Flashcards" para se adequar ao jargão educacional.

## 🚀 6. Conclusões e Próximos Passos

O experimento demonstrou que o **Fluent Horse tem Product-Market Fit em potencial**. A premissa de aprender através de notícias diárias engaja o usuário.

**Decisão do Experimento:** Ajustar (Refinar).

**Próximos Passos (Roadmap):**
1.  **Estabilização (Imediato):** Corrigir bugs de geração via IA e ajustar nomenclaturas e rotas de navegação (UX).
2.  **Expansão (Curto Prazo):** Adicionar botões de "Call to Action" diretos nas leituras e permitir a criação de baralhos maiores na ferramenta manual.
3.  **Engajamento (Médio Prazo):** Implementar o sistema de gamificação projetado (pontos, streaks, recompensas) para incentivar a retenção e a prática diária.

---
*Projeto desenvolvido para fins de estudo acadêmico e demonstração de arquitetura de software (Python Backend + React Frontend + Integração de IA).*
