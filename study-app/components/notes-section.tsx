"use client"

import { Button } from "@/components/ui/button"
import { Loader2 } from "lucide-react"

interface NotesSectionProps {
  notes: string
  onNotesChange: (notes: string) => void
  onGenerate: () => void
  isLoading: boolean
}

export function NotesSection({ notes, onNotesChange, onGenerate, isLoading }: NotesSectionProps) {
  return (
    <section className="w-full space-y-4">
      <label htmlFor="notes" className="sr-only">
        Study Notes
      </label>
      <textarea
        id="notes"
        value={notes}
        onChange={(e) => onNotesChange(e.target.value)}
        placeholder="Enter your study notes here..."
        className="w-full min-h-[200px] rounded-lg border border-input bg-card px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:border-transparent resize-y"
        rows={8}
      />
      <Button onClick={onGenerate} disabled={!notes.trim() || isLoading} className="w-full sm:w-auto">
        {isLoading ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Generating...
          </>
        ) : (
          "Generate Flashcards"
        )}
      </Button>
    </section>
  )
}
