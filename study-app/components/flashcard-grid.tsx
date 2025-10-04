"use client"

import { FlashCard } from "@/components/flash-card"

interface FlashcardGridProps {
  mode: "flashcards" | "quiz"
  cards: Array<{ id: number; question: string; answer: string }>
}

const sampleCards = [
  {
    id: 1,
    question: "What is the capital of France?",
    answer: "Paris",
  },
  {
    id: 2,
    question: "What is 2 + 2?",
    answer: "4",
  },
  {
    id: 3,
    question: 'Who wrote "Romeo and Juliet"?',
    answer: "William Shakespeare",
  },
  {
    id: 4,
    question: "What is the largest planet in our solar system?",
    answer: "Jupiter",
  },
  {
    id: 5,
    question: "What is the chemical symbol for water?",
    answer: "H₂O",
  },
  {
    id: 6,
    question: "In what year did World War II end?",
    answer: "1945",
  },
]

export function FlashcardGrid({ mode, cards }: FlashcardGridProps) {
  const displayCards = cards.length > 0 ? cards : sampleCards

  return (
    <section className="w-full">
      <h2 className="text-2xl font-semibold text-foreground mb-6">
        {mode === "flashcards" ? "Flashcards" : "Quiz Questions"}
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {displayCards.map((card) => (
          <FlashCard key={card.id} question={card.question} answer={card.answer} />
        ))}
      </div>
    </section>
  )
}
