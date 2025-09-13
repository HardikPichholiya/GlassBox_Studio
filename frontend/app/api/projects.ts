// Project-related client-side API helpers
import { api } from "./client";

export async function listProjects(): Promise<{ id: string; name: string }[]> {
  // Calls the backend to fetch projects; returns mock data if backend unavailable
  try {
    const { data } = await api.get("/api/projects");
    return data;
  } catch {
    return [
      { id: "demo-1", name: "Demo Project 1" },
      { id: "demo-2", name: "Demo Project 2" },
    ];
  }
}


