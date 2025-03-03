import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from PIL import Image, ImageTk
from io import BytesIO
import threading
import webbrowser

class Dota2StatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dota 2 Match Statistics")
        self.root.geometry("800x600")
        self.root.configure(bg="#1b1e23")
        
        # Set application icon and style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#1b1e23")
        self.style.configure("TLabel", background="#1b1e23", foreground="#ffffff")
        self.style.configure("TButton", background="#2c3e50", foreground="#ffffff")
        self.style.configure("Title.TLabel", background="#1b1e23", foreground="#ffffff", font=("Helvetica", 16, "bold"))
        self.style.configure("Subtitle.TLabel", background="#1b1e23", foreground="#dddddd", font=("Helvetica", 12))
        self.style.configure("Result.TLabel", background="#1b1e23", foreground="#5fba7d", font=("Helvetica", 14, "bold"))
        self.style.configure("ResultLoss.TLabel", background="#1b1e23", foreground="#e74c3c", font=("Helvetica", 14, "bold"))
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        ttk.Label(self.main_frame, text="Dota 2 Last Match Statistics", style="Title.TLabel").pack(pady=10)
        
        # Create input frame
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, pady=10)
        
        # Create Steam ID entry
        ttk.Label(self.input_frame, text="Enter Steam ID:").pack(side=tk.LEFT, padx=5)
        self.steam_id_var = tk.StringVar()
        self.steam_id_entry = ttk.Entry(self.input_frame, textvariable=self.steam_id_var, width=30)
        self.steam_id_entry.pack(side=tk.LEFT, padx=5)
        self.steam_id_entry.bind("<Return>", lambda event: self.fetch_stats())
        
        # Create fetch button
        self.fetch_button = ttk.Button(self.input_frame, text="Fetch Stats", command=self.fetch_stats)
        self.fetch_button.pack(side=tk.LEFT, padx=5)
        
        # Create loading indicator
        self.loading_var = tk.StringVar()
        self.loading_label = ttk.Label(self.input_frame, textvariable=self.loading_var)
        self.loading_label.pack(side=tk.LEFT, padx=5)
        
        # Create stats frame
        self.stats_frame = ttk.Frame(self.main_frame)
        self.stats_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create player info frame
        self.player_frame = ttk.Frame(self.stats_frame)
        self.player_frame.pack(fill=tk.X, pady=10)
        
        # Initialize player avatar
        self.avatar_label = ttk.Label(self.player_frame)
        self.avatar_label.pack(side=tk.LEFT, padx=10)
        
        # Player info
        self.player_info_frame = ttk.Frame(self.player_frame)
        self.player_info_frame.pack(side=tk.LEFT, padx=10, fill=tk.X)
        
        self.player_name_label = ttk.Label(self.player_info_frame, text="", style="Subtitle.TLabel")
        self.player_name_label.pack(anchor="w")
        
        self.match_result_label = ttk.Label(self.player_info_frame, text="")
        self.match_result_label.pack(anchor="w")
        
        # Match details frame
        self.match_frame = ttk.Frame(self.stats_frame)
        self.match_frame.pack(fill=tk.X, pady=10)
        
        # Hero frame
        self.hero_frame = ttk.Frame(self.match_frame)
        self.hero_frame.pack(side=tk.LEFT, padx=10)
        
        self.hero_image_label = ttk.Label(self.hero_frame)
        self.hero_image_label.pack()
        
        self.hero_name_label = ttk.Label(self.hero_frame, text="")
        self.hero_name_label.pack()
        
        # Match stats frame
        self.match_stats_frame = ttk.Frame(self.match_frame)
        self.match_stats_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Create performance metrics frame
        self.performance_frame = ttk.Frame(self.stats_frame)
        self.performance_frame.pack(fill=tk.X, pady=10)
        
        # Create three columns for performance metrics
        self.col1_frame = ttk.Frame(self.performance_frame)
        self.col1_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.col2_frame = ttk.Frame(self.performance_frame)
        self.col2_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.col3_frame = ttk.Frame(self.performance_frame)
        self.col3_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Match buttons frame
        self.match_buttons_frame = ttk.Frame(self.stats_frame)
        self.match_buttons_frame.pack(fill=tk.X, pady=10)
        
        self.match_id_var = tk.StringVar()
        self.match_id_label = ttk.Label(self.match_buttons_frame, textvariable=self.match_id_var)
        self.match_id_label.pack(side=tk.LEFT, padx=5)
        
        self.open_match_button = ttk.Button(
            self.match_buttons_frame, 
            text="Open in Browser", 
            command=self.open_match_in_browser
        )
        self.open_match_button.pack(side=tk.LEFT, padx=5)
        self.open_match_button.state(['disabled'])
        
        # Set example Steam ID
        self.steam_id_var.set("76561198063389763")  # Example Steam ID
        
        # Hero dictionary
        self.heroes = {}
        self.load_hero_data()
        
        # Current match ID
        self.current_match_id = None
    
    def load_hero_data(self):
        """Load hero data from OpenDota API"""
        try:
            response = requests.get("https://api.opendota.com/api/heroes")
            if response.status_code == 200:
                heroes_data = response.json()
                self.heroes = {hero['id']: hero for hero in heroes_data}
        except Exception as e:
            print(f"Error loading hero data: {e}")
    
    def fetch_stats(self):
        """Fetch player stats in a separate thread"""
        steam_id = self.steam_id_var.get().strip()
        if not steam_id:
            messagebox.showerror("Error", "Please enter a valid Steam ID")
            return
        
        self.loading_var.set("Loading...")
        self.fetch_button.state(['disabled'])
        self.clear_stats()
        
        threading.Thread(target=self._fetch_stats_thread, args=(steam_id,), daemon=True).start()
    
    def _fetch_stats_thread(self, steam_id):
        """Background thread for fetching stats"""
        try:
            # Convert Steam ID to account ID if needed
            if len(steam_id) > 10:
                try:
                    account_id = int(steam_id) - 76561197960265728
                except ValueError:
                    self.root.after(0, lambda: messagebox.showerror("Error", "Invalid Steam ID format"))
                    self.root.after(0, self._reset_loading)
                    return
            else:
                account_id = steam_id
                
            # Get player data
            player_response = requests.get(f"https://api.opendota.com/api/players/{account_id}")
            if player_response.status_code != 200:
                self.root.after(0, lambda: messagebox.showerror("Error", "Player not found"))
                self.root.after(0, self._reset_loading)
                return
                
            player_data = player_response.json()
            
            # Get recent matches
            recent_matches_response = requests.get(f"https://api.opendota.com/api/players/{account_id}/recentMatches")
            if recent_matches_response.status_code != 200 or not recent_matches_response.json():
                self.root.after(0, lambda: messagebox.showerror("Error", "No recent matches found"))
                self.root.after(0, self._reset_loading)
                return
                
            recent_matches = recent_matches_response.json()
            last_match = recent_matches[0]
            
            # Get full match details
            match_id = last_match['match_id']
            self.current_match_id = match_id
            match_response = requests.get(f"https://api.opendota.com/api/matches/{match_id}")
            if match_response.status_code != 200:
                self.root.after(0, lambda: messagebox.showerror("Error", "Match details not found"))
                self.root.after(0, self._reset_loading)
                return
                
            match_data = match_response.json()
            
            # Find player in match
            player_match_data = None
            for player in match_data['players']:
                if player['account_id'] == int(account_id):
                    player_match_data = player
                    break
                    
            if not player_match_data:
                self.root.after(0, lambda: messagebox.showerror("Error", "Player not found in match data"))
                self.root.after(0, self._reset_loading)
                return
                
            # Set player name
            player_name = player_data.get('profile', {}).get('personaname', 'Unknown')
            
            # Determine if player won
            player_slot = player_match_data['player_slot']
            radiant_win = match_data['radiant_win']
            is_radiant = player_slot < 128
            player_won = (is_radiant and radiant_win) or (not is_radiant and not radiant_win)
            
            # Get hero data
            hero_id = player_match_data['hero_id']
            hero_name = self.heroes.get(hero_id, {}).get('localized_name', 'Unknown Hero')
            
            # Get hero image
            hero_image_url = f"https://api.opendota.com/apps/dota2/images/heroes/{self.heroes.get(hero_id, {}).get('name', 'unknown')}_full.png"
            
            # Get player avatar
            avatar_url = player_data.get('profile', {}).get('avatarfull')
            
            # Display data on UI thread
            self.root.after(0, lambda: self.display_stats(
                player_name, 
                player_won,
                hero_name,
                hero_image_url,
                avatar_url,
                player_match_data,
                match_data
            ))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to fetch data: {e}"))
            self.root.after(0, self._reset_loading)
    
    def display_stats(self, player_name, player_won, hero_name, hero_image_url, avatar_url, player_data, match_data):
        """Display stats in the UI"""
        # Set player name
        self.player_name_label.config(text=player_name)
        
        # Set match result
        if player_won:
            self.match_result_label.config(text="Victory", style="Result.TLabel")
        else:
            self.match_result_label.config(text="Defeat", style="ResultLoss.TLabel")
            
        # Set match ID
        self.match_id_var.set(f"Match ID: {match_data['match_id']}")
        self.open_match_button.state(['!disabled'])
        
        # Display hero name
        self.hero_name_label.config(text=hero_name)
        
        # Load and display hero image
        self.load_image(hero_image_url, self.hero_image_label, (120, 68))
        
        # Load and display player avatar
        if avatar_url:
            self.load_image(avatar_url, self.avatar_label, (64, 64))
            
        # Clear previous stats
        for widget in self.match_stats_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col1_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col2_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col3_frame.winfo_children():
            widget.destroy()
            
        # Match duration
        duration_mins = match_data['duration'] // 60
        duration_secs = match_data['duration'] % 60
        ttk.Label(self.match_stats_frame, text=f"Duration: {duration_mins}:{duration_secs:02d}").pack(anchor="w")
        
        # Game mode
        game_mode = match_data.get('game_mode_name', 'Unknown')
        ttk.Label(self.match_stats_frame, text=f"Game Mode: {game_mode}").pack(anchor="w")
        
        # Match ended at
        start_time = match_data.get('start_time', 0)
        ttk.Label(self.match_stats_frame, text=f"Played on: {self.format_timestamp(start_time)}").pack(anchor="w")
        
        # Display KDA
        ttk.Label(self.col1_frame, text="K / D / A").pack(anchor="w")
        ttk.Label(self.col1_frame, text=f"{player_data['kills']} / {player_data['deaths']} / {player_data['assists']}", 
                  font=("Helvetica", 16, "bold")).pack(anchor="w")
        
        # Display GPM/XPM
        ttk.Label(self.col1_frame, text="GPM / XPM").pack(anchor="w")
        ttk.Label(self.col1_frame, text=f"{player_data['gold_per_min']} / {player_data['xp_per_min']}").pack(anchor="w")
        
        # Display last hits/denies
        ttk.Label(self.col2_frame, text="Last Hits / Denies").pack(anchor="w")
        ttk.Label(self.col2_frame, text=f"{player_data['last_hits']} / {player_data['denies']}").pack(anchor="w")
        
        # Display hero damage
        ttk.Label(self.col2_frame, text="Hero Damage").pack(anchor="w")
        ttk.Label(self.col2_frame, text=f"{player_data['hero_damage']:,}").pack(anchor="w")
        
        # Display tower damage
        ttk.Label(self.col3_frame, text="Tower Damage").pack(anchor="w")
        ttk.Label(self.col3_frame, text=f"{player_data['tower_damage']:,}").pack(anchor="w")
        
        # Display healing
        ttk.Label(self.col3_frame, text="Hero Healing").pack(anchor="w")
        ttk.Label(self.col3_frame, text=f"{player_data['hero_healing']:,}").pack(anchor="w")
        
        self._reset_loading()
    
    def load_image(self, url, label, size=None):
        """Load an image from URL and display in the given label"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                if size:
                    image = image.resize(size, Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                label.config(image=photo)
                label.image = photo  # Keep a reference
        except Exception as e:
            print(f"Error loading image: {e}")
    
    def clear_stats(self):
        """Clear all stats fields"""
        self.player_name_label.config(text="")
        self.match_result_label.config(text="")
        self.hero_name_label.config(text="")
        self.match_id_var.set("")
        self.open_match_button.state(['disabled'])
        
        # Clear images
        self.hero_image_label.config(image="")
        self.avatar_label.config(image="")
        
        # Clear stats
        for widget in self.match_stats_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col1_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col2_frame.winfo_children():
            widget.destroy()
            
        for widget in self.col3_frame.winfo_children():
            widget.destroy()
            
        self.current_match_id = None
    
    def _reset_loading(self):
        """Reset loading state"""
        self.loading_var.set("")
        self.fetch_button.state(['!disabled'])
    
    def format_timestamp(self, timestamp):
        """Format Unix timestamp to readable date"""
        from datetime import datetime
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M")
    
    def open_match_in_browser(self):
        """Open match details in web browser"""
        if self.current_match_id:
            webbrowser.open(f"https://www.opendota.com/matches/{self.current_match_id}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Dota2StatsApp(root)
    root.mainloop()