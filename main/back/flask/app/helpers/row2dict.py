def row2dict(row):
    return {c.name: getattr(row, c.name, None) for c in row.__table__.columns}