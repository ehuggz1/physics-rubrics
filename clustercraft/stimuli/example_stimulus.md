# Car Braking Scenario

## Situation

A 1000 kg car is traveling at 25 m/s on a wet pavement when the driver applies the brakes. The car comes to a complete stop after traveling 50 meters.

## Given Information

- Mass of car: m = 1000 kg
- Initial velocity: v₀ = 25 m/s
- Final velocity: v = 0 m/s
- Stopping distance: d = 50 m
- Coefficient of friction (wet pavement): μ = 0.3

## Motion Diagram

```mermaid
graph LR
    A[Car Moving<br/>v = 25 m/s] -->|Braking Applied| B[Decelerating<br/>a < 0]
    B -->|50 meters| C[Stopped<br/>v = 0 m/s]
    
    style A fill:#90EE90
    style B fill:#FFD700
    style C fill:#FF6B6B
```

## Force Diagram

```mermaid
graph TD
    subgraph "Forces on Car During Braking"
        N[Normal Force N<br/>↑]
        W[Weight mg<br/>↓]
        F[Friction Force f<br/>←]
    end
    
    style N fill:#87CEEB
    style W fill:#DDA0DD
    style F fill:#FFA07A
```

## Velocity vs. Time Data

```mermaid
graph LR
    subgraph "Velocity-Time Graph"
    end
```

| Time (s) | Velocity (m/s) | Position (m) | Acceleration (m/s²) |
|----------|----------------|--------------|---------------------|
| 0.0      | 25.0           | 0.0          | 0.0                 |
| 1.0      | 20.0           | 22.5         | -5.0                |
| 2.0      | 15.0           | 40.0         | -5.0                |
| 3.0      | 10.0           | 52.5         | -5.0                |
| 4.0      | 5.0            | 60.0         | -5.0                |
| 5.0      | 0.0            | 62.5         | -5.0                |

## Additional Context

The coefficient of friction between the wet pavement and the tires is approximately 0.3. The driver's reaction time before applying the brakes was 0.5 seconds.
