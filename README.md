# NASA SUITS Navigation & Rover AI Prototype

Run:
1. pip install -r requirements.txt
2. uvicorn app_nav:app --reload
3. Open http://127.0.0.1:8000

This prototype includes:
- localization stubs (IMU + beacon fusion)
- a simple SLAM stub that updates pose
- occupancy-grid mapping with synthetic obstacles
- A* path planner on grid
- Rover AI mission manager that executes plans
- Simple web UI for telemetry and map visualization
