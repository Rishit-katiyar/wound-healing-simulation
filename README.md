# Wound Healing Simulation 🩹💻

Welcome to the Wound Healing Simulation project! This Python simulation models the intricate process of wound healing, aiming to provide insights into the dynamic biological mechanisms involved in tissue repair. By incorporating principles such as chemotaxis, cell proliferation, differentiation, and apoptosis, the simulation offers a realistic representation of wound healing in biological systems. Through an interactive and visually appealing interface, users can observe how different factors influence the progression of wound healing over time. Whether you're a student exploring the fundamentals of biology or a researcher investigating tissue regeneration, this simulation serves as a valuable tool for understanding the complexities of wound healing in living organisms.

<p align="center">
  <img src="https://github.com/Rishit-katiyar/wound-healing-simulation/assets/167756997/ec8b3006-bef3-4d77-82ce-c840f942e3f4" alt="wound_healing_simulation" width="700"/>
</p>

### Chemotaxis:
Chemotaxis is the process by which cells migrate directionally in response to chemical gradients. In the wound healing simulation, cells exhibit chemotactic behavior, moving towards higher concentrations of signaling molecules released by neighboring cells or injured tissues. This mimics the natural response of cells to chemotactic factors such as growth factors, chemokines, and cytokines during wound healing.

### Cell Cycle Dynamics:
Cells undergo proliferation according to the cell cycle, a highly regulated process involving distinct phases such as G1, S, G2, and M phases. In the simulation, cells have specific probabilities of entering the cell cycle and proliferating based on local conditions. This reflects the dynamic nature of cell proliferation during wound healing, where cells actively divide to replenish damaged tissue.

### Differentiation:
Cell differentiation refers to the process by which cells become specialized and acquire distinct phenotypic characteristics. In the wound healing simulation, mesenchymal cells have the ability to differentiate into epithelial cells under appropriate signaling conditions. This represents tissue regeneration processes where undifferentiated cells contribute to the formation of specific cell types required for tissue repair.

### Apoptosis:
Apoptosis, or programmed cell death, plays a crucial role in tissue remodeling and homeostasis during wound healing. In the simulation, epithelial cells have a probability of undergoing apoptosis, leading to their removal from the tissue. This process helps regulate cell numbers, eliminate damaged or unnecessary cells, and promote tissue remodeling to restore normal tissue architecture.

### Inflammatory Response:
The initial phase of wound healing involves an inflammatory response characterized by immune cell infiltration and release of inflammatory cytokines. While not explicitly modeled in the simulation, the effects of inflammation are indirectly represented through the release of signaling molecules and interactions between different cell types.

### Extracellular Matrix Remodeling:
Cells interact with and remodel the extracellular matrix (ECM) during wound healing, influencing cell behavior and tissue architecture. While not directly simulated, the effects of ECM remodeling are indirectly captured through cell migration, proliferation, and differentiation processes. The simulation dynamics reflect the dynamic interplay between cells and the ECM during wound healing.

## Installation

Follow these steps to set up the simulation on your local machine:

### Prerequisites

- Python (>= 3.6)

### Clone the Repository

```bash
 git clone https://github.com/Rishit-katiyar/wound-healing-simulation.git
```

### Navigate to the Project Directory

```bash
cd wound-healing-simulation
```

### Install Dependencies

```bash
 pip install -r requirements.txt
```

## Usage

To run the simulation, execute the following command:

```bash
 python wound_healing_simulation.py
```

This will launch the simulation window where you can observe the wound healing process over time. You can adjust the simulation parameters and constants in the Python script to customize the behavior of the simulation.

## Features

- **Biologically Accurate**: Incorporates chemotaxis, cell cycle dynamics, differentiation, apoptosis, and other biological mechanisms involved in wound healing.
- **Customizable Parameters**: Easily modify simulation parameters and constants to explore different scenarios.
- **Realistic Visualization**: Uses a custom color scheme resembling human tissue colors for a visually appealing representation of the wound healing process.
- **Interactive Simulation**: Provides a dynamic and interactive simulation window to observe the progression of wound healing over time.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the fascinating processes of wound healing in biological systems.
- Built with Python, NumPy, and Matplotlib.
