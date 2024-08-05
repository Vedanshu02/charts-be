from app.api.plots import PlotRoute

plot_router_instance = PlotRoute()
plot_router = plot_router_instance.get_router()