from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

etudiants = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_etudiant():
    if request.method == 'POST':
        nom = request.form['nom']
        age = request.form['age']
        id_etudiant = request.form['id']
        notes = []

        etudiant = {"nom": nom, "age": age, "id": id_etudiant, "notes": notes}
        etudiants.append(etudiant)

        return redirect(url_for('afficher_etudiants'))
    
    return render_template('ajouter.html')

@app.route('/etudiants')
def afficher_etudiants():
    for etudiant in etudiants:
        notes_valides = [note['note'] for note in etudiant['notes'] if note['note'] != "abs"]
        etudiant['moyenne'] = sum(notes_valides) / len(notes_valides) if notes_valides else 0
    return render_template('etudiants.html', etudiants=etudiants)

@app.route('/etudiant/<id>')
def details_etudiant(id):
    etudiant = next((e for e in etudiants if e['id'] == id), None)
    if etudiant:
        notes_valides = [note['note'] for note in etudiant['notes'] if note['note'] != "abs"]
        moyenne = sum(notes_valides) / len(notes_valides) if notes_valides else 0
        return render_template('details.html', etudiant=etudiant, moyenne=moyenne)
    return "Étudiant non trouvé.", 404

@app.route('/ajouter_note/<id>', methods=['POST'])
def ajouter_note(id):
    etudiant = next((e for e in etudiants if e['id'] == id), None)
    if etudiant:
        matiere = request.form['matiere']
        absent = 'absent' in request.form

        if absent:
            etudiant['notes'].append({"matiere": matiere, "note": "abs"})
        else:
            note = request.form.get('note')
            if note:
                etudiant['notes'].append({"matiere": matiere, "note": float(note)})
            else:
                pass

    return redirect(url_for('details_etudiant', id=id))

@app.route('/modifier/<id>', methods=['GET', 'POST'])
def modifier_etudiant(id):
    etudiant = next((e for e in etudiants if e['id'] == id), None)
    if not etudiant:
        return "Étudiant non trouvé.", 404

    if request.method == 'POST':
        etudiant['nom'] = request.form['nom']
        etudiant['age'] = request.form['age']
        return redirect(url_for('afficher_etudiants'))
    
    return render_template('modifier.html', etudiant=etudiant)

@app.route('/supprimer/<id>')
def supprimer_etudiant(id):
    global etudiants
    etudiants = [e for e in etudiants if e['id'] != id]
    return redirect(url_for('afficher_etudiants'))

if __name__ == '__main__':
    app.run(debug=True)
