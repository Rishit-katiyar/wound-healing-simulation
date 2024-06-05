import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Define constants
WIDTH = 100
HEIGHT = 100
PROB_MIGRATION = 0.2
PROB_PROLIFERATION = 0.1
PROB_DIFFERENTIATION = 0.05
PROB_APOPTOSIS = 0.01
DIFFUSION_RATE = 0.1
GRADIENT_DECAY = 0.1
MAX_ITERATIONS = 200

# Define cell states
EMPTY = 0
EPITHELIAL = 1
MESENCHYMAL = 2
DEAD = 3

# Create a custom colormap resembling human tissue colors
tissue_colors = [(0.8, 0.8, 0.8), (0.9, 0.6, 0.6), (0.9, 0.7, 0.7), (0.6, 0.4, 0.4)]
tissue_cmap = LinearSegmentedColormap.from_list("tissue_cmap", tissue_colors)

# Initialize the grid, signaling molecule gradients, and other variables
grid = np.zeros((HEIGHT, WIDTH), dtype=int)
signaling_molecule = np.zeros((HEIGHT, WIDTH))

# Create initial wound from the outer edge towards the center
grid[:2, :] = EPITHELIAL
grid[-2:, :] = EPITHELIAL
grid[:, :2] = EPITHELIAL
grid[:, -2:] = EPITHELIAL

# Function to update the grid and signaling molecule gradients for each time step
def update_grid(frame_num, grid, signaling_molecule, img, txt):
    new_grid = grid.copy()
    new_signaling_molecule = signaling_molecule.copy()
    
    # Simulate diffusion of signaling molecules
    for y in range(HEIGHT):
        for x in range(WIDTH):
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if 0 <= y + dy < HEIGHT and 0 <= x + dx < WIDTH:
                        new_signaling_molecule[y, x] += (signaling_molecule[y + dy, x + dx] - signaling_molecule[y, x]) * DIFFUSION_RATE
    
    # Decay signaling molecule gradients
    new_signaling_molecule -= new_signaling_molecule * GRADIENT_DECAY
    
    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            if grid[y, x] == EMPTY:
                # Check neighboring cells for migration
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy != 0 or dx != 0) and 0 <= y + dy < HEIGHT and 0 <= x + dx < WIDTH:
                            if grid[y + dy, x + dx] == EPITHELIAL and np.random.rand() < PROB_MIGRATION:
                                new_grid[y, x] = EPITHELIAL
            elif grid[y, x] == MESENCHYMAL:
                # Check neighboring cells for proliferation
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy != 0 or dx != 0) and 0 <= y + dy < HEIGHT and 0 <= x + dx < WIDTH:
                            if grid[y + dy, x + dx] == EMPTY and np.random.rand() < PROB_PROLIFERATION:
                                new_grid[y + dy, x + dx] = MESENCHYMAL
                # Mesenchymal cells have a chance of differentiating into epithelial cells
                if np.random.rand() < PROB_DIFFERENTIATION:
                    new_grid[y, x] = EPITHELIAL
            elif grid[y, x] == EPITHELIAL:
                # Epithelial cells have a chance of undergoing apoptosis
                if np.random.rand() < PROB_APOPTOSIS:
                    new_grid[y, x] = DEAD
                    new_signaling_molecule[y, x] = 1  # Release signaling molecules upon apoptosis
    
    img.set_array(new_grid + signaling_molecule)
    grid[:] = new_grid[:]
    signaling_molecule[:] = new_signaling_molecule[:]
    
    # Update text annotation with simulation information
    txt.set_text(f'Time Step: {frame_num + 1}/{MAX_ITERATIONS}\n'
                 f'Epithelial Cells: {np.sum(new_grid == EPITHELIAL)}\n'
                 f'Mesenchymal Cells: {np.sum(new_grid == MESENCHYMAL)}\n'
                 f'Dead Cells: {np.sum(new_grid == DEAD)}')
    return img, txt

# Create animation
fig, ax = plt.subplots()
img = ax.imshow(grid + signaling_molecule, interpolation='nearest', cmap=tissue_cmap)
txt = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center', fontsize=12, color='black')
ani = animation.FuncAnimation(fig, update_grid, fargs=(grid, signaling_molecule, img, txt),
                              frames=MAX_ITERATIONS, interval=50, save_count=50)

plt.colorbar(img, label='Cell State + Signaling Molecule Concentration')
plt.title('Wound Healing Simulation')
plt.show()
