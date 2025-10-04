"use client"

import { useState } from "react"
import { Card } from "@/components/ui/card"

interface FlashCardProps {
  question: string
  answer: string
}

export function FlashCard({ question, answer }: FlashCardProps) {
  const [isFlipped, setIsFlipped] = useState(false)

  return (
    <div className="relative h-64 cursor-pointer perspective-1000" onClick={() => setIsFlipped(!isFlipped)}>
      <div
        className={`relative w-full h-full transition-transform duration-500 transform-style-3d ${
          isFlipped ? "rotate-y-180" : ""
        }`}
        style={{
          transformStyle: "preserve-3d",
          transform: isFlipped ? "rotateY(180deg)" : "rotateY(0deg)",
        }}
      >
        {/* Front of card */}
        <Card
          className="absolute inset-0 flex items-center justify-center p-6 backface-hidden bg-card border-border"
          style={{ backfaceVisibility: "hidden" }}
        >
          <div className="text-center">
            <p className="text-sm text-muted-foreground mb-2">Question</p>
            <p className="text-lg font-medium text-card-foreground text-balance">{question}</p>
          </div>
        </Card>

        {/* Back of card */}
        <Card
          className="absolute inset-0 flex items-center justify-center p-6 backface-hidden bg-primary border-border"
          style={{
            backfaceVisibility: "hidden",
            transform: "rotateY(180deg)",
          }}
        >
          <div className="text-center">
            <p className="text-sm text-primary-foreground/80 mb-2">Answer</p>
            <p className="text-lg font-medium text-primary-foreground text-balance">{answer}</p>
          </div>
        </Card>
      </div>
    </div>
  )
}
