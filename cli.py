import click
import json_utils

@click.group()
def cli():
  pass

@cli.command()
def users():
  users = json_utils.read_json()
  for user in users:
    print(f"{user['id']} - {user['name']} - {user['lastname']}")
    
@cli.command()
@click.option('--name', required=True, help='Nombre del usuario')
@click.option('--lastname', required=True, help='Apellido del usuario')
@click.pass_context
def create(ctx, name, lastname):
  if not name or not lastname:
    ctx.fail('El nombre y apellido son requeridos')
  else:
    data = json_utils.read_json()
    new_id = len(data) +1
    new_user = {
      'id': new_id,
      'name': name,
      'lastname': lastname
    }
    data.append(new_user)
    json_utils.write_json(data)
    print(f"Usuario {name} {lastname} creado correctamente")

@cli.command()
@click.argument('id', type=int)
def user(id):
  data = json_utils.read_json()
  user = next((x for x in data if x['id'] == id), None)
  if user is None:
    print("El usuario no fue encontrado")
  else:
    print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def delete(id):
  data = json_utils.read_json()
  user = next((x for x in data if x['id'] == id), None)
  if user is None:
    print("El usuario no fue encontrado")
  else:
    data.remove(user)
    json_utils.write_json(data)
    print(f"Usuario eliminado correctamente")

if __name__ == '__main__':
  cli()