from fastapi import APIRouter, HTTPException, Query
from app.database import supabase
from typing import Optional
import random

router = APIRouter()

@router.get("/players")
def get_players(
    country: Optional[str] = Query(None),
    role: Optional[str] = Query(None),
    ipl_team: Optional[str] = Query(None),
    name: Optional[str] = Query(None)
):
    query = supabase.table("players").select("*")

    if country:
        query = query.ilike("country", f"%{country}%")
    if role:
        query = query.ilike("role", f"%{role}%")
    if ipl_team:
        query = query.ilike("ipl_team", f"%{ipl_team}%")
    if name:
        query = query.ilike("name", f"%{name}%")

    response = query.execute()
    return {
        "status": "success",
        "count": len(response.data),
        "data": response.data
    }

@router.get("/players/random")
def get_random_player():
    response = supabase.table("players").select("*").execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="No players found")
    player = random.choice(response.data)
    return {
        "status": "success",
        "data": player
    }

@router.get("/players/{player_id}")
def get_player(player_id: int):
    response = supabase.table("players").select("*").eq("id", player_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Player not found")
    return {
        "status": "success",
        "data": response.data[0]
    }