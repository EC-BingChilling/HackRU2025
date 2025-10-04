"use client"

const GEMINI_KEY ="AIzaSyDlB87G2CQrIeJrl7icoEnwAcvaUbXwaJE"
const ELEVEN_KEY ="sk_22c6139d91d1d74e79d9a7a6434bce261319de20868c1c68"

const BACKEND_URL = "http://localhost:5000"

import { useState } from "react"
import { NotesSection } from "@/components/notes-section"
import { StudyModeSelector } from "@/components/study-mode-selector"
import { FlashcardGrid } from "@/components/flashcard-grid"
import { AudioPlayer } from "@/components/audio-player"

type Card = {
  id: number
  question: string
  answer: string
}

export default function StudyPage() {
  const [notes, setNotes] = useState("")
  const [studyMode, setStudyMode] = useState<"flashcards" | "quiz">("flashcards")
  const [cards, setCards] = useState<Card[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const handleGenerate = async () => {
    if (!notes.trim()) return

    setIsLoading(true)
    try {
      const response = await fetch(`${BACKEND_URL}/generate?key=${GEMINI_KEY}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: notes }),
      })

      if (!response.ok) {
        throw new Error("Failed to generate cards")
      }

      const data = await response.json()
      setCards(data)
    } catch (error) {
      console.error("Error generating cards:", error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="space-y-8">
          {/* Notes Section */}
          <NotesSection notes={notes} onNotesChange={setNotes} onGenerate={handleGenerate} isLoading={isLoading} />

          {/* Study Mode Selector */}
          <StudyModeSelector mode={studyMode} onModeChange={setStudyMode} />

          {/* Flashcard Grid */}
          <FlashcardGrid mode={studyMode} cards={cards} />

          {/* Audio Player */}
          <AudioPlayer />
        </div>
      </div>
    </main>
  )
}
