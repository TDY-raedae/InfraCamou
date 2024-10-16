## NightWalker: Robust Multi-view Infrared Adversarial Attack with Physically Realizable Camouflage via Voronoi Diagrams

![alt text](pipline.png)



## Abstract
Thermal infrared object detection based on deep neural networks (DNNs) is widely used for safety-critical tasks in dark scenes, but exhibits misbehavior and even results in irreversible disasters. Therefore, it is crucial to estimate the vulnerability of DNN-based thermal infrared systems and improve their security. The adversarial attack based on physically realizable camouflage is one of the most appealing ways to identify their vulnerability, which crafts adversarial patches adding to the object to fool DNN-based thermal infrared systems into being blind. However, existing attacks are still limited from three aspects: viewing restriction, transformation loss, and attention-grabbing. To address these issues, we propose NightWalker, a new physical infrared camouflage framework that differs from previous works: (1) multi-view - it alleviates the viewing restriction in physical domain through 3D-to-2D projection loss optimization based on Voronoi diagrams; (2) robustness - it degrades the transformation loss from the digital to the physical domain by developing Expectation Over Transformation for infrared contrast; (3) stealthiness - it avoids attention-grabbing in visible and infrared scenes through color smoothing and emissivity-controllable materials automatic determination. Extensive evaluations across 3 datasets, 8 detectors, and 10 materials demonstrate NightWalker’s superior performance against 8 baselines in 50 subjects The demos are available at this page.



