"use client"

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

interface StudyModeSelectorProps {
  mode: "flashcards" | "quiz"
  onModeChange: (mode: "flashcards" | "quiz") => void
}

export function StudyModeSelector({ mode, onModeChange }: StudyModeSelectorProps) {
  return (
    <section className="w-full">
      <label htmlFor="study-mode" className="block text-sm font-medium text-foreground mb-2">
        Study Mode
      </label>
      <Select value={mode} onValueChange={(value) => onModeChange(value as "flashcards" | "quiz")}>
        <SelectTrigger id="study-mode" className="w-full sm:w-64 bg-card">
          <SelectValue placeholder="Select study mode" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="flashcards">Flashcards</SelectItem>
          <SelectItem value="quiz">Quiz</SelectItem>
        </SelectContent>
      </Select>
    </section>
  )
}
