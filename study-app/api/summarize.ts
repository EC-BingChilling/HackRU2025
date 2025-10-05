import { NextApiRequest, NextApiResponse } from "next";

type Body = { text: string };

let history: { input: string; summary: string }[] = [];

export default function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === "POST") {
        const { text } = req.body as Body;
        const summary = text.slice(0, 100) + (text.length > 100 ? "…" : "");
        history.push({ input: text, summary });
        res.status(200).json({ summary });
    } else if (req.method === "GET") {
        res.status(200).json(history);
    } else {
        res.status(405).end();
    }
}
