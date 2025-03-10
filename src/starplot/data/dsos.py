from enum import Enum

messier = {
    "M1": (5.575547, 22.014472),
    "M2": (21.557503, 0.823306),
    "M3": (13.703119, 28.375444),
    "M4": (16.393167, -25.474472),
    "M5": (15.309375, 2.082694),
    "M6": (17.672431, -31.745833),
    "M7": (17.89755, -33.207167),
    "M8": (18.061464, -23.619833),
    "M9": (17.319939, -17.48375),
    "M10": (16.952497, -3.900667),
    "M11": (18.851664, -5.729972),
    "M12": (16.787367, -0.052167),
    "M13": (16.694897, 36.461306),
    "M14": (17.626711, -2.754083),
    "M15": (21.49955, 12.166833),
    "M16": (18.313381, -12.192778),
    "M17": (18.346419, -15.828472),
    "M18": (18.332914, -16.898028),
    "M19": (17.0438, -25.732056),
    "M20": (18.045031, -21.028111),
    "M21": (18.070403, -21.509944),
    "M22": (18.606722, -22.096583),
    "M23": (17.951325, -17.014667),
    "M24": (18.282256, -17.485444),
    "M25": (18.529658, -18.885056),
    "M26": (18.755183, -8.616389),
    "M27": (19.993439, 22.721028),
    "M28": (18.409136, -23.130167),
    "M29": (20.399381, 38.507667),
    "M30": (21.672783, -22.820917),
    "M31": (0.712319, 41.269056),
    "M32": (0.711619, 40.865278),
    "M33": (1.564136, 30.660222),
    "M34": (2.702056, 42.746139),
    "M35": (6.151406, 24.338639),
    "M36": (5.604928, 34.14075),
    "M37": (5.871764, 32.553),
    "M38": (5.478469, 35.854917),
    "M39": (21.530089, 48.438167),
    "M40": (12.371139, 58.084444),
    "M41": (6.76665, -19.245778),
    "M42": (5.587911, -4.610333),
    "M43": (5.59205, -4.732528),
    "M44": (8.672833, 19.672056),
    "M45": (3.791278, 24.105278),
    "M46": (7.696339, -13.19),
    "M47": (7.609728, -13.517389),
    "M48": (8.228661, -4.249556),
    "M49": (12.496322, 8.000472),
    "M50": (7.044575, -7.635972),
    "M51": (13.497975, 47.195167),
    "M52": (23.413444, 61.593167),
    "M53": (13.215342, 18.169111),
    "M54": (18.917575, -29.5215),
    "M55": (19.6665, -29.037917),
    "M56": (19.276531, 30.1845),
    "M57": (18.893058, 33.028583),
    "M58": (12.628756, 11.818194),
    "M59": (12.700622, 11.647028),
    "M60": (12.727772, 11.552694),
    "M61": (12.36525, 4.473639),
    "M62": (17.020167, -29.887639),
    "M63": (13.263703, 42.029278),
    "M64": (12.945456, 21.682972),
    "M65": (11.315533, 13.092361),
    "M66": (11.337489, 12.991528),
    "M67": (8.855592, 11.811944),
    "M68": (12.657781, -25.256972),
    "M69": (18.523119, -31.652028),
    "M70": (18.720178, -31.708111),
    "M71": (19.896142, 18.778389),
    "M72": (20.891086, -11.462944),
    "M73": (20.982214, -11.3645),
    "M74": (1.611597, 15.783667),
    "M75": (20.101344, -20.077778),
    "M76": (1.705469, 51.575472),
    "M77": (2.711308, 0.013278),
    "M78": (5.779394, 0.079306),
    "M79": (5.402942, -23.475778),
    "M80": (16.284031, -21.024889),
    "M81": (9.925881, 69.065306),
    "M82": (9.931314, 69.679389),
    "M83": (13.616931, -28.134583),
    "M84": (12.417706, 12.886972),
    "M85": (12.423364, 18.1915),
    "M86": (12.436594, 12.946222),
    "M87": (12.513728, 12.391111),
    "M88": (12.5331, 14.420389),
    "M89": (12.594392, 12.556333),
    "M90": (12.613831, 13.162944),
    "M91": (12.590681, 14.496333),
    "M92": (17.285353, 43.136528),
    "M93": (7.741453, -22.146917),
    "M94": (12.848072, 41.120444),
    "M95": (10.732694, 11.703806),
    "M96": (10.779372, 11.819944),
    "M97": (11.246586, 55.019028),
    "M98": (12.230081, 14.900333),
    "M99": (12.313778, 14.4165),
    "M100": (12.381897, 15.821806),
    "M101": (14.053483, 54.348944),
    "M103": (1.556058, 60.658),
    "M104": (12.666508, -10.376944),
    "M105": (10.797108, 12.581611),
    "M106": (12.315972, 47.303972),
    "M107": (16.5422, -12.946361),
    "M108": (11.191936, 55.674111),
    "M109": (11.959994, 53.374528),
    "M110": (0.6728, 41.685306),
}

ZENITH_BASE = [
    "M5",
    "M13",
    "M23",
    "M31",
    "M42",
    "M44",
    "M45",
    "M47",
    "M51",
    "M55",
    "M83",
    "M93",
    "M104",
]


class DsoType(str, Enum):
    """
    Types of deep sky objects (DSOs), as designated in OpenNGC
    """

    STAR = "Star"
    DOUBLE_STAR = "Double star"
    ASSOCIATION_OF_STARS = "Association of stars"

    OPEN_CLUSTER = "Open Cluster"
    GLOBULAR_CLUSTER = "Globular Cluster"

    GALAXY = "Galaxy"
    GALAXY_PAIR = "Galaxy Pair"
    GALAXY_TRIPLET = "Galaxy Triplet"
    GROUP_OF_GALAXIES = "Group of galaxies"

    NEBULA = "Nebula"
    PLANETARY_NEBULA = "Planetary Nebula"
    EMISSION_NEBULA = "Emission Nebula"
    STAR_CLUSTER_NEBULA = "Star cluster + Nebula"
    REFLECTION_NEBULA = "Reflection Nebula"

    DARK_NEBULA = "Dark Nebula"
    HII_IONIZED_REGION = "HII Ionized region"
    SUPERNOVA_REMNANT = "Supernova remnant"
    NOVA_STAR = "Nova star"
    NONEXISTENT = "Nonexistent object"
    UNKNOWN = "Object of other/unknown type"
    DUPLICATE_RECORD = "Duplicated record"


ONGC_TYPE = {
    # Star Clusters ----------
    DsoType.OPEN_CLUSTER: "OCl",
    DsoType.GLOBULAR_CLUSTER: "GCl",
    # Galaxies ----------
    DsoType.GALAXY: "G",
    DsoType.GALAXY_PAIR: "GPair",
    DsoType.GALAXY_TRIPLET: "GTrpl",
    DsoType.GROUP_OF_GALAXIES: "GGroup",
    # Nebulas ----------
    DsoType.NEBULA: "Neb",
    DsoType.PLANETARY_NEBULA: "PN",
    DsoType.EMISSION_NEBULA: "EmN",
    DsoType.STAR_CLUSTER_NEBULA: "Cl+N",
    DsoType.REFLECTION_NEBULA: "RfN",
    # Stars ----------
    DsoType.STAR: "*",
    DsoType.DOUBLE_STAR: "**",
    DsoType.ASSOCIATION_OF_STARS: "*Ass",
    # Others - not supported yet (no styles defined)
    DsoType.HII_IONIZED_REGION: "HII",
    DsoType.DARK_NEBULA: "DrkN",
    DsoType.SUPERNOVA_REMNANT: "SNR",
    DsoType.NOVA_STAR: "Nova",
    DsoType.NONEXISTENT: "NonEx",
    DsoType.UNKNOWN: "Other",
    DsoType.DUPLICATE_RECORD: "Dup",
}

ONGC_TYPE_MAP = {v: k.value for k, v in ONGC_TYPE.items()}

DEFAULT_DSO_TYPES = [
    # Star Clusters ----------
    DsoType.OPEN_CLUSTER,
    DsoType.GLOBULAR_CLUSTER,
    # Galaxies ----------
    DsoType.GALAXY,
    DsoType.GALAXY_PAIR,
    DsoType.GALAXY_TRIPLET,
    DsoType.GROUP_OF_GALAXIES,
    # Nebulas ----------
    DsoType.NEBULA,
    DsoType.PLANETARY_NEBULA,
    DsoType.EMISSION_NEBULA,
    DsoType.STAR_CLUSTER_NEBULA,
    DsoType.REFLECTION_NEBULA,
    # Stars ----------
    # DsoType.DOUBLE_STAR,
    DsoType.ASSOCIATION_OF_STARS,
]
"""Default types of Deep Sky Objects (DSOs) that are plotted on maps"""

LEGEND_LABELS = {
    # Galaxies ----------
    DsoType.GALAXY: "Galaxy",
    DsoType.GALAXY_PAIR: "Galaxy",
    DsoType.GALAXY_TRIPLET: "Galaxy",
    DsoType.GROUP_OF_GALAXIES: "Galaxy",
    # Nebulas ----------
    DsoType.NEBULA: "Nebula",
    DsoType.PLANETARY_NEBULA: "Nebula",
    DsoType.EMISSION_NEBULA: "Nebula",
    DsoType.STAR_CLUSTER_NEBULA: "Nebula",
    DsoType.REFLECTION_NEBULA: "Nebula",
}
